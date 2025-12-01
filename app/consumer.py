from kafka import KafkaConsumer
import json

KAFKA_BOOTSTRAP_SERVERS = "localhost:9092"
TOPIC_NAME = "weather"

def main():
    consumer = KafkaConsumer(
        TOPIC_NAME,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        value_deserializer=lambda m: json.loads(m.decode("utf-8")),
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        group_id="weather-group"
    )

    print(f"Starting weather consumer on topic '{TOPIC_NAME}'...\n")

    for msg in consumer:
        print("Received:", msg.value)

if __name__ == "__main__":
    main()
