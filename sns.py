import boto3
import json


def file_move_sns():
    region = "us-west-2"
    email = "ssystem32@gmail.com"

    sns = boto3.client("sns", region_name=region)
    sts = boto3.client("sts", region_name=region)

    # 1. Get current AWS Account ID
    account_id = sts.get_caller_identity()["Account"]

    # 2. Create SNS Topic
    res = sns.create_topic(Name="file-move-alert")
    topic_arn = res["TopicArn"]

    # 3. Subscribe email
    sns.subscribe(TopicArn=topic_arn, Protocol="email", Endpoint=email)
    print(f"\n~ Subscription request sent...\n")

    # 4. Set custom policy to require authentication to unsubscribe
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
