import boto3
import os

print("\nPreparing to upload all the sales reports from the report folder...\n")


sales_folder = "./reports"
bucket_name1 = "sales-report-document"
prefix = "customer-details/"

s3 = boto3.client("s3")

print("\nUploading to the 'sales-report-document' bucket...\n")
print("\nCreating 'customer-details' folder...\n")

for file_name in os.listdir(sales_folder):
    full_path = os.path.join(sales_folder, file_name)

    s3_key = f"{prefix}{file_name}"

    s3.upload_file(full_path, bucket_name1, s3_key)
    print(f"> {file_name} successfully uploaded!")


print("\n*** Process finished successfully ***\n")
