
import pika

EXCHANGE_NAME = "ecommerce_events"


def get_connection():
    return pika.BlockingConnection(
        pika.ConnectionParameters(host="localhost")
    )


def setup_exchange(channel):
    channel.exchange_declare(
        exchange=EXCHANGE_NAME,
        exchange_type="topic",
        durable=True
    )
