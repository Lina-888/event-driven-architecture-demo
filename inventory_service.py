
import json

from rabbitmq import EXCHANGE_NAME, get_connection, setup_exchange


def handle_event(ch, method, properties, body):
    event = json.loads(body)
    event_type = event["event_type"]
    order_id = event["order_id"]

    print(f"\n[Inventory Service] Received {event_type}")
    print(f"Order ID: {order_id}")

    if event_type == "OrderPlaced":
        print("[Inventory Service] Updating stock...")

    elif event_type == "OrderCancelled":
        print("[Inventory Service] Restoring stock...")

    ch.basic_ack(delivery_tag=method.delivery_tag)


def main():
    connection = get_connection()
    channel = connection.channel()

    setup_exchange(channel)

    channel.queue_declare(
        queue="inventory_queue",
        durable=True
    )

    channel.queue_bind(
        exchange=EXCHANGE_NAME,
        queue="inventory_queue",
        routing_key="OrderPlaced"
    )

    channel.queue_bind(
        exchange=EXCHANGE_NAME,
        queue="inventory_queue",
        routing_key="OrderCancelled"
    )

    channel.basic_qos(prefetch_count=1)

    channel.basic_consume(
        queue="inventory_queue",
        on_message_callback=handle_event
    )

    print("[Inventory Service] Waiting for events...")
    print("Subscribed to: OrderPlaced, OrderCancelled")

    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print("\n[Inventory Service] Stopped")
    finally:
        if connection.is_open:
            connection.close()


if __name__ == "__main__":
    main()
