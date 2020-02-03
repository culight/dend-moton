import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries
import json
from aws_client import aws_client

def create_cluster(config):
    # initialize aws client
    sparkify_client = aws_client(config)

    # initialize resources and clients
    sparkify_client.init_resources(['ec2', 's3'])
    sparkify_client.init_clients(['iam', 'redshift'])

    # initialize buckets
    sparkify_client.init_buckets(
        ['udacity-dend/song_data', 'udacity-dend/log_data']
    )

    # initialize role
    policy_doc = json.dumps(
        {'Statement': [{'Action': 'sts:AssumeRole',
                'Effect': 'Allow',
                'Principal': {'Service': 'redshift.amazonaws.com'}}],
                'Version': '2012-10-17'})
    policy = 'arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess'
    sparkify_client.init_role(policy, policy_doc)

    # initialize cluster and vpc
    sparkify_client.init_cluster()
    sparkify_client.init_vpc()

    return sparkify_client


def drop_tables(cur, conn):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    sparkify_client = create_cluster(config)

    conn = psycopg2.connect(
        "host={} dbname={} user={} password={} port={}".format(
            sparkify_client.host,
            sparkify_client.config['db'],
            sparkify_client.config['user'],
            sparkify_client.config['password'],
            sparkify_client.config['port']
        )
    )
    cur = conn.cursor()

    drop_tables(cur, conn)
    # create_tables(cur, conn)

    conn.close()
    sparkify_client.disconnect()


if __name__ == "__main__":
    main()