# AWS S3 Automation with SNS Notifications

This project automates the process of:

- Creating two S3 buckets
- Uploading files from a local directory
- Moving specific files (`sr1`) to another bucket
- Sending email notifications via Amazon SNS

## 🧱 Project Structure

```
.
├── controller.py            # Main script to run all others in order
├── sns.py                  # SNS topic creation and email notification
├── createBuckets.py        # Creates the required S3 buckets
├── upload_files.py         # Uploads files from ./reports to a bucket
├── list_and_move.py        # Moves specific files and sends notification
├── .gitignore              # Git ignore config
```

## ✅ Requirements

- Python 3.x
- `boto3` installed
- AWS credentials configured (`~/.aws/credentials`)
- IAM user with permission to use S3 and SNS

Install dependencies:
```bash
pip install boto3
```

## 🚀 How to Run

1. **Prepare files**  
   Place your sales report files inside a local `./reports` folder.

2. **Start the automation**
   ```bash
   python3 controller.py
   ```

   The script will:
   - Ask if you're subscribed to SNS
   - Send a subscription email if not
   - Create 2 buckets
   - Upload files
   - Move `sr1` files and notify via email

3. **Email Confirmation**  
   If not already subscribed, check your email and confirm the subscription before proceeding.

## 📬 SNS Email Setup

The default recipient email is set in `sns.py`:
```python
email = "system32j@gmail.com"
```

Change it to your preferred email address.

## 🪪 Bucket Names Used

- `sales-report-document`
- `sales-report-document-sr1`

Ensure these names are unique per AWS region or modify them accordingly.

## 📦 What Gets Uploaded

All files in `./reports/` are uploaded to:
```
sales-report-document/customer-details/
```

## 🔄 What Gets Moved

Only files containing `'sr1'` in their key are:
- Moved to `sales-report-document-sr1`
- Deleted from the original bucket
- Trigger a notification

## 📌 Notes

- Make sure your AWS credentials are valid and active.
- All operations are done in the `us-west-2` region.

---

**Happy Automating!**
