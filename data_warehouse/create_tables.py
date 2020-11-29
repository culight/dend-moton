# ----------------------------------------------------------------
# Author: Demerrick Moton
# Summary: Wrapper for AWS Data Warehousing Sparkify hosting and management
# ----------------------------------------------------------------
import logging
import json

import configparser
import psycopg2
from aws_client import aws_client

from sql_queries import (
    create_table_queries,
    drop_table_queries,
    copy_table_queries,
    insert_table_queries,
)

logging.basicConfig(
    filename="create_table.py",
    level=logging.DEBUG,
    format="%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
LOGGER = logging.getLogger("create_tables")

# ----------------------------------------------------------------
# Source code is below, Constants and Imports are above
# ----------------------------------------------------------------


def create_cluster(config):
    """ Initialize the cluster"""

    # initialize aws client
    LOGGER.debug("initializing AWS resources")
    sparkify_client = aws_client(config)

    # initialize resources and clients
    sparkify_client.init_resources(["ec2", "s3"])
    sparkify_client.init_clients(["iam", "redshift"])

    # initialize buckets
    sparkify_client.init_buckets(["udacity-dend/song_data", "udacity-dend/log_data"])

    # initialize role
    policy_doc = json.dumps(
        {
            "Statement": [
                {
                    "Action": "sts:AssumeRole",
                    "Effect": "Allow",
                    "Principal": {"Service": "redshift.amazonaws.com"},
                }
            ],
            "Version": "2012-10-17",
        }
    )
    policy = "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess"
    sparkify_client.init_role(policy, policy_doc)

    # initialize cluster and vpc
    sparkify_client.init_cluster()
    # sparkify_client.init_vpc()

    LOGGER.debug("Done initializing AWS resources")

    return sparkify_client


def drop_tables(cur, conn):
    """Remove tables from database"""
    LOGGER.debug("clearing existing tables")
    for query in drop_table_queries:
        cur.execute(query)
    conn.commit()


def create_tables(cur, conn):
    """Create the tables in the database"""
    LOGGER.debug("creating tables")
    for query in create_table_queries:
        cur.execute(query)
    conn.commit()


def copy_data(cur, conn):
    """Copt data into the staging tables"""
    LOGGER.debug("copying data from S3")
    for query in copy_table_queries:
        LOGGER.debug("copying data...")
        cur.execute(query)
    conn.commit()


def insert_tables(cur, conn):
    """Insert data into other tables from staging tables"""
    for query in insert_table_queries:
        cur.execute(query)
    conn.commit()


def main():
    """Main function housing the high level execution of the code"""
    # setup configuration
    config = configparser.ConfigParser()
    config.read("dwh.cfg")

    # connect to aws client
    sparkify_client = create_cluster(config)

    # connect to redshift db
    conn = psycopg2.connect(
        "host={} dbname={} user={} password={} port={}".format(
            sparkify_client.host,
            sparkify_client.config["db"],
            sparkify_client.config["user"],
            sparkify_client.config["password"],
            sparkify_client.config["port"],
        )
    )
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)
    copy_data(cur, conn)
    insert_tables(cur, conn)

    conn.close()
    sparkify_client.disconnect()


if __name__ == "__main__":
    main()
