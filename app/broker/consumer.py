
# from kafka import KafkaConsumer


# def consumer():
#     topic_name = 'query'
#     consumer = KafkaConsumer(topic_name, auto_offset_reset='earliest',
#                              bootstrap_servers=['localhost:9092'], api_version=(0, 10), consumer_timeout_ms=1000)
#     return consumer

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '/Users/tinuade/Downloads/marvis-vdohmu-2777cc606436.json'

from google.cloud import pubsub_v1

project_id = "marvis-vdohmu"
subscription_name = "consumer"
timeout = 5.0  # "How long the subscriber should listen for
# messages in seconds"

subscriber = pubsub_v1.SubscriberClient()
# The `subscription_path` method creates a fully qualified identifier
# in the form `projects/{project_id}/subscriptions/{subscription_name}`
subscription_path = subscriber.subscription_path(
    project_id, subscription_name
)


def callback(message):
    print("Received message: {}".format(message))
    message.ack()


def consumer():
    streaming_pull_future = subscriber.subscribe(
        subscription_path, callback=callback
    )
    print("Listening for messages on {}..\n".format(subscription_path))

    # result() in a future will block indefinitely if `timeout` is not set,
    # unless an exception is encountered first.
    try:
        data = streaming_pull_future.result(timeout=timeout)
        print(data)
        data = dict(data)
        return data
    except:  # noqa
        streaming_pull_future.cancel()
