import boto3
if __name__ == '__main__':
    s3_resource = boto3.resource("s3")
    object = s3_resource.Object(bucket_name="infyni",
                                key="icons.txt")
    object.upload_file("c:/icons.txt")