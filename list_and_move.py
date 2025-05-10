import boto3

print(
    "\n******\n\nListing all the objects from 'sr1',\ninside the 'sales-report-document' bucket,\nin the 'customer-details' folder...\n\n******\n"
)

bucket_name1 = "sales-report-document"
folder_prefix = "customer-details/"
dest_bucket = "sales-report-document-sr1"

s3 = boto3.client("s3")

all_objects = s3.list_objects_v2(Bucket=bucket_name1, Prefix=folder_prefix)

i = 1
if_sr1 = False

for obj in all_objects["Contents"]:
    if 'sr1' in obj['Key']:
        if_sr1 = True
        print(f"\n{i}. {obj}\n")

        copy_source = {
            "Bucket": bucket_name1,  # Source bucket name
            "Key": obj["Key"],  # Key (filename with path) to copy
        }

        print("\n> Moving file to 'sales-report-document-sr1' bucket...")
        s3.copy(copy_source, dest_bucket, obj["Key"])
        s3.delete_object(Bucket=bucket_name1, Key=obj["Key"])
        i += 1

if not if_sr1:
    print("\n*** No sr1 files found, process completed! ***\n")
else:
    print("\n*** Moving and deleting the files completed! ***\n")
