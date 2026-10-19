
import json
import sys
from datetime import datetime, timezone

import pika

from rabbitmq import EXCHANGE_NAME, get_connection, setup_exchange


def publish_event(event_type, order_id):
    connection = get_connection()

    try:
        channel = connection.channel()
        setup_exchange(channel)

        event = {
            "event_type": event_type,
            "order_id": order_id,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }

        channel.basic_publish(
            exchange=EXCHANGE_NAME,
            routing_key=event_type,
            body=json.dumps(event),
            properties=pika.BasicProperties(
                delivery_mode=2,
                content_type="application/json"
            )
        )

        print(f"[Order Service] Published {event_type}")
        print(f"Order ID: {order_id}")
    finally:
        connection.close()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python producer.py <event_type> <order_id>")
        sys.exit(1)

    publish_event(sys.argv[1], sys.argv[2])
