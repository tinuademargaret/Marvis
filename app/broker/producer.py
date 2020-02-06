# from kafka import KafkaProducer

"""
single node kafka broker
"""


# def publish_message(producer_instance, topic_name, key, value):
#     try:
#         key_bytes = bytes(key, encoding='utf-8')
#         value_bytes = bytes(value, encoding='utf-8')
#         producer_instance.send(topic_name, key=key_bytes, value=value_bytes)
#         producer_instance.flush()
#         print('Message published successfully.')
#     except Exception as ex:
#         print('Exception in publishing message')
#         print(str(ex))


# def connect_kafka_producer():
#     _producer = None
#     try:
#         _producer = KafkaProducer(bootstrap_servers=['localhost:9092'], api_version=(0, 10))
#     except Exception as ex:
#         print('Exception while connecting Kafka')
#         print(str(ex))
#     finally:
#         return _producer


# def produce(command):
#     try:
#         kafka_producer = connect_kafka_producer()
#         action = command.action
#         query = command.query
#         publish_message(kafka_producer, 'query', action, query)
#         if kafka_producer is not None:
#             kafka_producer.close()
#     except Exception as e:
#         print('Exception while producing'+str(e))
#
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
