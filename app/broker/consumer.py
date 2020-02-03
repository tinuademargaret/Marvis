
from kafka import KafkaConsumer


def consumer():
    topic_name = 'query'
    consumer = KafkaConsumer(topic_name, auto_offset_reset='earliest',
                             bootstrap_servers=['localhost:9092'], api_version=(0, 10), consumer_timeout_ms=1000)
    return consumer






