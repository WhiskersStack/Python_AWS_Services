import boto3

print("\n************ Creating Two Buckets ************\n")

bucket_name1 = 'dct-sales'
bucket_name2 = 'dct-sales-sr1'
region = 'us-west-2'

client = boto3.client("s3")

