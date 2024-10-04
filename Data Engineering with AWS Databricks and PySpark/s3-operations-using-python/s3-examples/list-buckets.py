import boto3
session = boto3.Session()
s3 = session.client("s3")
for bucket in s3.list_buckets()["Buckets"]:
    print(bucket["Name"])
