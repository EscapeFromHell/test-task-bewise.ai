from datetime import datetime

import sqlalchemy.orm as so
from sqlalchemy import func

from src.core.models.base import Base
from src.core.schemas import Application as ApplicationSchema


class Application(Base):
    __tablename__ = "applications"
    id: so.Mapped[int] = so.mapped_column(primary_key=True, index=True)
    user_name: so.Mapped[str] = so.mapped_column(index=True, nullable=False)
    description: so.Mapped[str] = so.mapped_column(nullable=False)
    created_at: so.Mapped[datetime] = so.mapped_column(server_default=func.now(), nullable=False)

    def to_pydantic_schema(self) -> ApplicationSchema:
        return ApplicationSchema(
            id=self.id, user_name=self.user_name, description=self.description, created_at=self.created_at
        )
