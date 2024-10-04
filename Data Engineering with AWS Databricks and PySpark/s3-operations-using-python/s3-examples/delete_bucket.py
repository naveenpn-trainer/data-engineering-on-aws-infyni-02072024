import boto3
s3_resource = boto3.resource("s3")
bucket = s3_resource.Bucket("infynibatch05")
bucket.delete()