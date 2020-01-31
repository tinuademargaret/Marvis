from kafka import KafkaProducer
from app.services.parser import parser


def publish_message(producer_instance, topic_name, key, value):
    try:
        key_bytes = bytes(key, encoding='utf-8')
        value_bytes = bytes(value, encoding='utf-8')
        producer_instance.send(topic_name, key=key_bytes, value=value_bytes)
        producer_instance.flush()
        print('Message published successfully.')
    except Exception as ex:
        print('Exception in publishing message')
        print(str(ex))


def connect_kafka_producer():
    _producer = None
    try:
        _producer = KafkaProducer(bootstrap_servers=['localhost:9092'], api_version=(0, 10))
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))
    finally:
        return _producer


def produce():
    command = parser()
    try:
        kafka_producer = connect_kafka_producer()
        publish_message(kafka_producer, 'product', 'command', command)
        if kafka_producer is not None:
            kafka_producer.close()
    except Exception as e:
        print('Exception while producing'+e)

