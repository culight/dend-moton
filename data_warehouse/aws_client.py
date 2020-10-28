import boto3
from botocore.exceptions import ClientError
import pandas as pd
import time

# ----------------------------------------------------------------
# Source code is below, Constants and Imports are above
# ----------------------------------------------------------------


class aws_client:
    def __init__(self, config):
        self._load_config(config)

    def _load_config(self, config):
        self.config = {}

        self.config["key"] = config.get("AWS", "KEY")
        self.config["secret"] = config.get("AWS", "SECRET")

        self.config["cluster_type"] = config.get("DWH", "DWH_CLUSTER_TYPE")
        self.config["num_nodes"] = config.get("DWH", "DWH_NUM_NODES")
        self.config["node_type"] = config.get("DWH", "DWH_NODE_TYPE")

        self.config["cluster_id"] = config.get("DWH", "DWH_CLUSTER_ID")
        self.config["db"] = config.get("DWH", "DWH_DB")
        self.config["user"] = config.get("DWH", "DWH_DB_USER")
        self.config["password"] = config.get("DWH", "DWH_DB_PASSWORD")
        self.config["port"] = config.get("DWH", "DWH_PORT")

        self.config["iam_role_name"] = config.get("DWH", "DWH_IAM_ROLE")
        self.config["region"] = config.get("DWH", "DWH_REGION")

    def init_resources(self, resource_names):
        assert resource_names, "Provide list of aws services to be initialized"
        self.resources = {}
        for resource_name in resource_names:
            print("Initializing {} service".format(resource_name))
            self.resources[resource_name] = boto3.resource(
                resource_name,
                region_name=self.config["region"],
                aws_access_key_id=self.config["key"],
                aws_secret_access_key=self.config["secret"],
            )

        return self.resources

    def init_clients(self, client_names):
        assert client_names, "Provide list of aws services to be initialized"
        self.clients = {}
        for client_name in client_names:
            print("Initializing {} service".format(client_name))
            self.clients[client_name] = boto3.client(
                client_name,
                region_name=self.config["region"],
                aws_access_key_id=self.config["key"],
                aws_secret_access_key=self.config["secret"],
            )

        return self.clients

    def init_buckets(self, bucket_names):
        assert bucket_names, "Provide list of bucket names to be initialized"
        self.buckets = {}
        for bucket_name in bucket_names:
            print("Initializing {} bucket".format(bucket_name))
            self.buckets[bucket_name] = self.resources["s3"].Bucket(bucket_name)

        return self.buckets

    def init_role(self, policy, policy_doc, description=""):
        # get role if it already exists, otherwise create one
        self.role = None
        try:
            self.role = self.clients["iam"].get_role(
                RoleName=self.config["iam_role_name"]
            )
        except Exception:
            try:
                print("Creating a new IAM Role")
                self.role = self.clients["iam"].create_role(
                    Path="/",
                    RoleName=self.config["iam_role_name"],
                    Description=description,
                    AssumeRolePolicyDocument=policy_doc,
                )
            except Exception as e:
                print(e)

        print("Attaching Policy")
        assert self.role, "IAM role name not created"
        self.clients["iam"].attach_role_policy(
            RoleName=self.config["iam_role_name"], PolicyArn=policy
        )["ResponseMetadata"]["HTTPStatusCode"]

        print("Get the IAM role ARN")
        self.role_arn = self.clients["iam"].get_role(
            RoleName=self.config["iam_role_name"]
        )["Role"]["Arn"]

        print(self.role_arn)

        return self.role, self.role_arn

    def init_cluster(self):
        try:
            self.cluster = self.clients["redshift"].describe_clusters(
                ClusterIdentifier=self.config["cluster_id"]
            )["Clusters"][0]

        except Exception:
            try:
                response = self.clients["redshift"].create_cluster(
                    # HW
                    ClusterType=self.config["cluster_type"],
                    NodeType=self.config["node_type"],
                    # Identifiers & Credentials
                    DBName=self.config["db"],
                    ClusterIdentifier=self.config["cluster_id"],
                    MasterUsername=self.config["user"],
                    MasterUserPassword=self.config["password"],
                    # Roles (for s3 access)
                    IamRoles=[self.role_arn],
                )
                print(response)
                self.cluster = self.clients["redshift"].describe_clusters(
                    ClusterIdentifier=self.config["cluster_id"]
                )["Clusters"][0]
            except Exception as e:
                print(e)

        self.host = None
        count = 0
        while (
            self.clients["redshift"].describe_clusters(
                ClusterIdentifier=self.config["cluster_id"]
            )["Clusters"][0]["ClusterAvailabilityStatus"]
            != "Available"
        ):
            print("waiting for cluster to be created...")
            time.sleep(30)
            if count >= 20:
                # wait for 10 minutes
                print("Timeout while waiting to create cluster")
                return self.cluster
            else:
                count += 1

        # get params not that cluster is avialable
        self.cluster = self.clients["redshift"].describe_clusters(
            ClusterIdentifier=self.config["cluster_id"]
        )["Clusters"][0]
        self.host = self.cluster["Endpoint"]["Address"]

        return self.cluster

    def print_cluster_props(self):
        assert self.cluster, "Cluster not created"
        pd.set_option("display.max_colwidth", -1)
        keysToShow = [
            "ClusterIdentifier",
            "NodeType",
            "ClusterStatus",
            "MasterUsername",
            "DBName",
            "Endpoint",
            "NumberOfNodes",
            "VpcId",
        ]
        x = [(k, v) for k, v in self.cluster.items() if k in keysToShow]
        return pd.DataFrame(data=x, columns=["Key", "Value"])

    def init_vpc(self):
        try:
            self.resources["vpc"] = self.resources["ec2"].Vpc(id=self.cluster["VpcId"])
            defaultSg = list(self.resources["vpc"].security_groups.all())[0]
            print(defaultSg)
            defaultSg.authorize_ingress(
                GroupName=defaultSg.group_name,
                CidrIp="172.31.0.0/16",
                IpProtocol="TCP",
                FromPort=int(self.config["port"]),
                ToPort=int(self.config["port"]),
            )
        except Exception as e:
            print(e)

        return self.resources["vpc"]

    def disconnect(self):
        policies = self.clients["iam"].list_role_policies(
            RoleName=self.config["iam_role_name"]
        )["PolicyNames"]
        for policy in policies:
            self.clients["iam"].detach_role_policy(
                RoleName=self.config["iam_role_name"], PolicyArn=policy,
            )
            time.sleep(3)
        self.clients["redshift"].delete_cluster(
            ClusterIdentifier=self.config["cluster_id"], SkipFinalClusterSnapshot=True
        )
        self.clients["iam"].delete_role(RoleName=self.config["iam_role_name"])
