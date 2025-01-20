from typing import Sequence

from sqlalchemy import select

from src.core.models import Application
from src.core.repository.repository import SqlAlchemyRepository


class ApplicationsRepository(SqlAlchemyRepository):
    model = Application

    async def get_applications(self, user_name: str, page: int, size: int) -> Sequence[Application]:
        """
        Retrieve a list of applications based on username and pagination parameters.
        """
        base_query = select(self.model)
        if user_name:
            base_query = base_query.filter(self.model.user_name == user_name)
        base_query = base_query.offset((page - 1) * size).limit(size)
        query = await self.session.execute(base_query)
        results = query.scalars().all()
        return results

    async def create_application(self, application: Application) -> Application:
        """
        Create a new application in the database.
        """
        async with self.session.begin():
            self.session.add(application)
        return application
