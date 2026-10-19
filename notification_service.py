
import json

from rabbitmq import EXCHANGE_NAME, get_connection, setup_exchange


def handle_event(ch, method, properties, body):
    event = json.loads(body)
    event_type = event["event_type"]
    order_id = event["order_id"]

    print(f"\n[Notification Service] Received {event_type}")
    print(f"Order ID: {order_id}")

    if event_type == "OrderPlaced":
        print("[Notification Service] Sending order confirmation...")

    elif event_type == "OrderShipped":
        print("[Notification Service] Sending shipping notification...")

    ch.basic_ack(delivery_tag=method.delivery_tag)


def main():
    connection = get_connection()
    channel = connection.channel()

    setup_exchange(channel)

    channel.queue_declare(
        queue="notification_queue",
        durable=True
    )

    for event_type in ["OrderPlaced", "OrderShipped"]:
        channel.queue_bind(
            exchange=EXCHANGE_NAME,
            queue="notification_queue",
            routing_key=event_type
        )

    channel.basic_qos(prefetch_count=1)

    channel.basic_consume(
        queue="notification_queue",
        on_message_callback=handle_event
    )

    print("[Notification Service] Waiting for events...")
    print("Subscribed to: OrderPlaced, OrderShipped")

    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print("\n[Notification Service] Stopped")
    finally:
        if connection.is_open:
            connection.close()


if __name__ == "__main__":
    main()
