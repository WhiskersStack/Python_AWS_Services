import boto3

print("\n************ Creating Two Buckets ************\n")

bucket_name1 = "sales-report-document"
bucket_name2 = "sales-report-document-sr1"
region = "us-west-2"

client = boto3.client("s3", region_name=region)


def create_bucket(bucket_name):
    try:
        client.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={"LocationConstraint": "us-west-2"},
        )
        print("\n~ Bucket created successful!\n")
    except Exception as e:
        print(f"\n~ Failed to create a bucket - {e}\n")


print("\nAttempting to create the first bucket 'sales-report-document'...\n")
create_bucket(bucket_name1)
print("\nAttempting to create the first bucket 'sales-report-document-sr1'...\n")
create_bucket(bucket_name2)

print("\n******** Creating process finished ********\n")
