# Irrigation Pi Backend

A Python backend application using FastAPI.

## Database
The application uses a [SQLite](https://www.sqlite.org/) database as the application meant to be run on an Raspberry Pi.
Migrations are managed with [Alembic](https://alembic.sqlalchemy.org/).

Create initial migrations:
```shell
alembic revision --autogenerate -m "Initial Migrations"
```
Create database:
```shell
alembic upgrade head
```
