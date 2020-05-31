import os
from google.cloud import pubsub_v1
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '/Users/tinuade/Downloads/marvis-vdohmu-2777cc606436.json'

project_id = "marvis-vdohmu"
topic_name = "query"

publisher = pubsub_v1.PublisherClient()
# The `topic_path` method creates a fully qualified identifier
# in the form `projects/{project_id}/topics/{topic_name}`
topic_path = publisher.topic_path(project_id, topic_name)


def produce(command):
    data = str(command)
    # Data must be a bytestring
    data = data.encode("utf-8")
    # When you publish a message, the client returns a future.
    future = publisher.publish(topic_path, data=data)
    print(future.result())
    print("Published messages.")
