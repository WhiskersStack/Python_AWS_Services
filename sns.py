import boto3

region = "us-west-2"
email = "system32j@gmail.com"

sns = boto3.client("sns", region_name=region)
res = sns.create_topic(Name="file-move-alert")
topic_arn = res["TopicArn"]

subject = "Files Moved"
message = "All the sr1 files moved"


def file_move_sns():
    sns.subscribe(TopicArn=topic_arn, Protocol="email", Endpoint=email)
    print(f"\n~ Subscription request sent...\n")

if __name__ == "__main__":
    file_move_sns()


def move_alert():
    response = sns.publish(TopicArn=topic_arn, Subject=subject, Message=message)

    print(f"\nSNS sent\n\n")
