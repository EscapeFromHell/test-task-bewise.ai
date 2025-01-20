import logging

from src.config import kafka
from src.core.models import Application
from src.core.schemas import Application as ApplicationSchema
from src.core.schemas import ApplicationCreate
from src.core.service.service import BaseService
from src.core.uow import UnitOfWork
from src.utils import get_logger

logger = get_logger(__file__, logging.INFO)


class ApplicationsService(BaseService):
    base_repository: str = "applications"

    @staticmethod
    async def __send_message_to_kafka(created_application: ApplicationSchema) -> None:
        """
        Send a message to Kafka topic with the details of a newly created application.
        """
        message = {
            "id": created_application.id,
            "user_name": created_application.user_name,
            "description": created_application.description,
            "created_at": created_application.created_at.isoformat(),
        }
        logger.info(f"Sending message to Kafka: {message}")
        await kafka.kafka_producer.send_and_wait(kafka.KAFKA_TOPIC, str(message).encode("utf-8"))
        logger.info("Message successfully sent to Kafka")

    @classmethod
    async def get_applications(
        cls, user_name: str | None, page: int, size: int, uow: UnitOfWork
    ) -> list[ApplicationSchema]:
        """
        Retrieve a list of applications based on username and pagination parameters.
        """
        async with uow:
            result = await uow.__dict__[cls.base_repository].get_applications(user_name=user_name, page=page, size=size)
        applications = [application.to_pydantic_schema() for application in result]
        logger.info(f"Successfully retrieved {len(applications)} applications")
        return applications

    @classmethod
    async def create_application(
        cls,
        application: ApplicationCreate,
        uow: UnitOfWork,
    ) -> ApplicationSchema:
        """
        Create a new application in the database and send a message to Kafka.
        """
        application_model = Application(user_name=application.user_name, description=application.description)
        async with uow:
            result = await uow.__dict__[cls.base_repository].create_application(application=application_model)
        logger.info("Created application")
        created_application = result.to_pydantic_schema()
        await cls.__send_message_to_kafka(created_application=created_application)
        return created_application
