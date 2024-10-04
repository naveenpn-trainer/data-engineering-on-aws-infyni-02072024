import boto3
if __name__ == '__main__':
    s3_resource = boto3.resource("s3")
    my_bucket = s3_resource.Bucket("infyni")
    for object in my_bucket.objects.all():
        print(object)