import aiokafka


class KafkaConfig:
    kafka_producer = None
    KAFKA_BROKER: str = "kafka:9092"
    KAFKA_TOPIC: str = "applications"

    @classmethod
    async def initialize(cls):
        if cls.kafka_producer is None:
            cls.kafka_producer = aiokafka.AIOKafkaProducer(bootstrap_servers=cls.KAFKA_BROKER)
            await cls.kafka_producer.start()

    @classmethod
    async def shutdown(cls):
        if cls.kafka_producer:
            await cls.kafka_producer.stop()
            cls.kafka_producer = None


kafka = KafkaConfig()
