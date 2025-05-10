import boto3

print(
    "\nListing all the objects inside the 'sales-report-document' bucket, in the 'customer-details' folder...\n"
)
bucket_name1 = "sales-report-document"
folder_prefix = "customer-details/"

s3 = boto3.client("s3")

all_objects = s3.list_objects_v2(Bucket=bucket_name1, Prefix=folder_prefix)

i = 1
for obj in all_objects["Contents"]:
    print(f"\n{i}. {obj}\n")
    i += 1

i = 1
print("\nListing all the files inside the folder...\n")
for obj in all_objects["Contents"]:
    print(f"{i}. {obj['Key']}")
    i += 1
