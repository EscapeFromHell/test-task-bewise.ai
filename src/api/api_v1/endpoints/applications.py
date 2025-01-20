from fastapi import APIRouter, Depends, Query

from src.core.schemas import Application, ApplicationCreate
from src.core.service.applications import ApplicationsService
from src.core.uow import UnitOfWork

router = APIRouter()


@router.post("/", status_code=201, response_model=Application)
async def create_application(application: ApplicationCreate, uow: UnitOfWork = Depends(UnitOfWork)) -> Application:
    """
    Create a new application in the database and send a message to Kafka.
    """
    return await ApplicationsService.create_application(application=application, uow=uow)


@router.get("/", status_code=200, response_model=list[Application])
async def get_applications(
    user_name: str = Query(None),
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100),
    uow: UnitOfWork = Depends(UnitOfWork),
) -> list[Application]:
    """
    Retrieve a list of applications based on the provided filters.
    """
    return await ApplicationsService.get_applications(user_name=user_name, page=page, size=size, uow=uow)
