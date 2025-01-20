from datetime import datetime

from pydantic import BaseModel, PositiveInt


class ApplicationBase(BaseModel):
    user_name: str
    description: str
    created_at: datetime


class ApplicationCreate(ApplicationBase):
    pass


class ApplicationUpdate(ApplicationBase):
    pass


class ApplicationInDB(ApplicationBase):
    id: PositiveInt

    class Config:
        from_attributes = True


class Application(ApplicationInDB):
    pass
