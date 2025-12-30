import logging

from confluent_kafka import Producer

logger = logging.getLogger(__name__)


def delivery_report(err, msg):
    if err:
        logger.error(f"Message delivery failed: {err}")
    else:
        logger.info(f"Message delivered: topic={msg.topic()} key={msg.key()}")


class KafkaProducer:
    def __init__(self, servers: str):
        self.producer = Producer(
            {
                "bootstrap.servers": servers,
                "delivery.timeout.ms": 3000,
                "request.timeout.ms": 1000,
                "retries": 2,
                "queue.buffering.max.messages": 100000,
                "queue.buffering.max.kbytes": 10240,
                "acks": "all",
            }
        )

    def send(self, topic: str, key: str, value: dict):
        try:
            self.producer.produce(
                topic=topic,
                key=key,
                value=value,
                on_delivery=delivery_report,
            )
            self.producer.poll(0)
        except Exception as e:
            logger.error(f"Failed to send message: {e}")
