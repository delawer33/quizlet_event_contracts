from kafka_producer import KafkaProducer

producer = KafkaProducer("localhost:9092")

producer.send("learning.events", key=str(1), value={1: 2})
