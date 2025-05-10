import boto3
import json

region = "us-west-2"
email = "ssystem32@gmail.com"

sns = boto3.client("sns", region_name=region)
sts = boto3.client("sts", region_name=region)

account_id = sts.get_caller_identity()["Account"]
res = sns.create_topic(Name="file-move-alert")
topic_arn = res["TopicArn"]

subject = "Files Moved"
message = "All the sr1 files moved"


def file_move_sns():

    sns.subscribe(TopicArn=topic_arn, Protocol="email", Endpoint=email)
    print(f"\n~ Subscription request sent...\n")

    policy = {
        "Version": "2008-10-17",
        "Statement": [
            {
                "Sid": "AllowOwnerAccess",
                "Effect": "Allow",
                "Principal": {"AWS": "*"},
                "Action": ["SNS:Subscribe", "SNS:Receive"],
                "Resource": topic_arn,
                "Condition": {"StringEquals": {"AWS:SourceOwner": account_id}},
            },
            {
                "Sid": "AllowPublish",
                "Effect": "Allow",
                "Principal": {"AWS": "*"},
                "Action": "SNS:Publish",
                "Resource": topic_arn,
            },
        ],
    }

    sns.set_topic_attributes(
        TopicArn=topic_arn, AttributeName="Policy", AttributeValue=json.dumps(policy)
    )


file_move_sns()


def move_alert():
    sns = boto3.client("sns", region_name="us-west-2")

    response = sns.publish(TopicArn=topic_arn, Subject=subject, Message=message)

    print(f"\nSNS sent\n\n")
