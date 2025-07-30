from datetime import datetime

from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def send_kafka_log(event: str, data: dict):
    log = {
        "event": event,
        "data": data,
        "time": datetime.now().isoformat(),
    }
    producer.send("user-events", value=log)
    producer.flush()
