import boto3


def get_aws_configured_region():
    session = boto3.session.Session()
    return session.region_name


if __name__ == '__main__':
    s3_resource = boto3.resource("s3")

    configured_region = get_aws_configured_region()
    print(configured_region)
    bucket_configurations = {"LocationConstraint": configured_region}
    s3_resource.create_bucket(Bucket="infyni",
                              CreateBucketConfiguration=bucket_configurations)
