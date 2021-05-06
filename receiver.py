import boto3
import time
import sys
import json

sqs       = boto3.client('sqs')
queue_url = ''

while True:
  try:
    response  = sqs.receive_message(
                  QueueUrl=queue_url,
                  MaxNumberOfMessages=1,
                  MessageAttributeNames=['All'],
                  VisibilityTimeout=0,
                  WaitTimeSeconds=0
                )

    #print(json.dumps(response, indent=1))

    if response.get('Messages'):
      message   = response['Messages'][0]
      messageId = message['MessageId']
      createdAt = message['MessageAttributes']['CreatedAt']['StringValue']
      content   = message['Body']

      print("[{} {}]: {}".format(messageId, createdAt, content))

      # Delete the message
      receiptHandle = message['ReceiptHandle']

      sqs.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=receiptHandle
      )

  except KeyboardInterrupt:
    print('')
    sys.exit(0)
  except Exception as e:
    print(e)
    print("\nSomething went wrong...")
    print(json.dumps(response, indent=1))
