from kafka import KafkaProducer
import json
import time
import random
from datetime import datetime

KAFKA_BOOTSTRAP_SERVERS = "localhost:9092"
TOPIC_NAME = "weather"

def create_producer():
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )
    return producer

def generate_weather_event():
    cities = ["Paris", "London", "Berlin", "Madrid", "Rome", "Lisbon", "Dublin", "Amsterdam"]
    event = {
        "city": random.choice(cities),
        "temp": round(random.uniform(-5, 35), 1),
        "humidity": random.randint(20, 100),
        "ts": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return event

def main():
    producer = create_producer()
    print(f"Starting weather producer on topic '{TOPIC_NAME}'...\n")

    while True:
        event = generate_weather_event()
        producer.send(TOPIC_NAME, event)
        producer.flush()
        print("Sent:", event)
        time.sleep(2)

if __name__ == "__main__":
    main()
