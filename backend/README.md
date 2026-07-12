# Irrigation Pi Backend

A Python backend application using FastAPI.

## Installation for Development
This installation section is meant for software engineers which like to do contributions to the project.
If you are an end user who just wants to install Irrigation-Pi on your Raspberry Pi, you can ignore this section. 

### uv
[Install uv](https://docs.astral.sh/uv/getting-started/installation/) on your machine, i.e.:
```shell
curl -LsSf https://astral.sh/uv/install.sh | sh
```

In project root install Python package dependencies with uv and create a virtual environment:
```shell
uv sync
```

### Database
The application uses a [SQLite](https://www.sqlite.org/) database as the application meant to be run on an Raspberry Pi.
Migrations are managed with [Alembic](https://alembic.sqlalchemy.org/).

After creating the virtual environment you are able to use the project's management CLI to install the database.
Activate virtual environment, then install the [SQLite](https://www.sqlite.org/) database:
```shell
source .venv/bin/activate
irrigation-pi install database
```

Start the backend application:
```shell
irrigation-pi run backend
```
The backend application is running afterwards and is accessible on: http://0.0.0.0:8000/api 
