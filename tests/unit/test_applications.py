import pytest
import httpx
from datetime import datetime


@pytest.mark.asyncio
async def test_create_application():
    payload = {"user_name": "Test username", "description": "Test application", "created_at": datetime.now().isoformat()}
    async with httpx.AsyncClient() as client:
        response = await client.post(
            url="http://127.0.0.1:8000/api_v1/applications/",
            headers={"Content-Type": "application/json"},
            json=payload,
        )
    assert response.status_code == 201
    data = response.json()
    assert data["user_name"] == "Test username"
    assert data["description"] == "Test application"
    assert "id" in data
    assert "created_at" in data


@pytest.mark.asyncio
async def test_filter_applications():
    async with httpx.AsyncClient() as client:
        response = await client.get(
            url="http://127.0.0.1:8000/api_v1/applications/",
            headers={"Content-Type": "application/json"},
            params={"user_name": "Test username", "page": 1, "size": 100})
    assert response.status_code == 200
    data = response.json()
    assert data[0]["user_name"] == "Test username"
    assert data[0]["description"] == "Test application"
