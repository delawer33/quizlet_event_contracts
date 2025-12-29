import logging

from confluent_kafka import Producer

logger = logging.getLogger(__name__)


class KafkaProducer:
    def __init__(self, servers: str):
        self.producer = Producer(
            {
                "bootstrap.servers": servers,
                "acks": "all",
            }
        )

    def send(self, topic: str, key: str, value: dict):
        try:
            self.producer.produce(
                topic=topic,
                key=key,
                value=value,
            )
            self.producer.flush()
        except Exception as e:
            logger.error(f"Failed to send message: {e}")
