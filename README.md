# Sample app for SQS

## Requirements

* python 3.x
* boto3

## Installation

```
pip install -r requirements.txt
```

Make sure to change the `queue_url` value in `sender.py` and `receiver.py` with your own queue location.

## Sender

```
python sender.py
```

## Receiver

```
python receiver.py
```
