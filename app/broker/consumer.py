
from kafka import KafkaConsumer


def consume():
    parsed_topic_name = 'product'
    consumer = KafkaConsumer(parsed_topic_name, auto_offset_reset='earliest',
                             bootstrap_servers=['localhost:9092'], api_version=(0, 10), consumer_timeout_ms=1000)
    return consumer
