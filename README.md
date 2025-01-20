# Bewise.ai

## Applications FastAPI
### В сервисе реализовано:
- Принятие заявки.
- Запись в БД (PostgreSQL).
- Отправление сообщение в Kafka о создании новой заявки.
- Получение заявок с фильтрацией по имени пользователей и пагинацией.

### Эндпоинты:

- POST /api_v1/applications: Создание заявки.
- GET /api_v1/applications: Получение списка заявок (фильтрация по username и пагинация).

#### Пример POST запроса:

{
  "user_name": "user_name",
  "description": "description",
  "created_at": "2025-01-19T11:45:39.923Z"
}

#### Пример ответа:

{
  "user_name": "user_name",
  "description": "description",
  "created_at": "2025-01-19T11:45:39.923Z",
  "id": 1
}



#### Пример GET запроса:
user_name: "user_name"


#### Пример ответа:


[{
    "user_name": "user_name",
    "description": "description",
    "created_at": "2025-01-19T11:45:39.923Z",
    "id": 1 }]

## Технологии
Python, FastAPI, Pydantic, SQLAlchemy, Alembic, PostgreSQL, Kafka, Docker

## Запуск проекта
- Скачайте проект: git clone https://github.com/EscapeFromHell/test-task-bewise.ai.git
- После скачивания проекта, перейдите в папку проекта: cd test-task-bewise.ai
- Выполните команду: docker compose up -d
- После запуска контейнеров, интерактивная документация будет доступна по ссылке: http://127.0.0.1:8000/docs
