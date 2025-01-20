from copy import deepcopy
from typing import Callable

import pytest
from sqlalchemy import insert, text, delete

from src.core.models import Application
from src.core.schemas import ApplicationCreate
from tests.fakes import FAKES_APPLICATIONS


@pytest.fixture(scope="function")
def applications() -> list[ApplicationCreate]:
    return deepcopy(FAKES_APPLICATIONS)


@pytest.fixture(scope="session")
def clean_applications(async_session_maker) -> Callable:
    async def _clean_applications():
        async with async_session_maker() as session:
            await session.execute(delete(Application))
            await session.execute(text("ALTER SEQUENCE applications_id_seq RESTART WITH 1;"))
            await session.commit()

    return _clean_applications


@pytest.fixture(scope="function")
def add_applications(async_session_maker, applications) -> Callable:
    async def _add_applications() -> None:
        async with async_session_maker() as session:
            for applications_schema in applications:
                await session.execute(insert(Application).values(**applications_schema.model_dump()))
            await session.commit()

    return _add_applications
