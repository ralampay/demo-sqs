import boto3
import sys
from datetime import datetime

sqs       = boto3.client('sqs')
queue_url = ''

while True:
  try:
    message = input("Enter message: ")
    print("Sending: {}...".format(message))

    response  = sqs.send_message(
                  QueueUrl=queue_url,
                  DelaySeconds=10,
                  MessageAttributes={
                    'CreatedAt': {
                      'DataType': 'String',
                      'StringValue': str(datetime.now())
                    }
                  },
                  MessageBody=(message)
                )

    print(response)

  except KeyboardInterrupt:
    print('')
    sys.exit(0)
  except Exception as e:
    print(e)
    print("\nSomething went wrong...")
