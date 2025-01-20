from datetime import datetime

from src.core.schemas import ApplicationCreate


FAKES_APPLICATIONS = [
    ApplicationCreate(user_name="Test User 1", description="Test application 1", created_at=datetime.now().isoformat()),
    ApplicationCreate(user_name="Test User 2", description="Test application 2", created_at=datetime.now().isoformat()),
    ApplicationCreate(user_name="Test User 3", description="Test application 3", created_at=datetime.now().isoformat())
]
