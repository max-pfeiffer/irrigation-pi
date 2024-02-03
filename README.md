[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![codecov](https://codecov.io/gh/max-pfeiffer/irrigation-pi/graph/badge.svg?token=Tk9STeqlPn)](https://codecov.io/gh/max-pfeiffer/irrigation-pi)
![pipeline workflow](https://github.com/max-pfeiffer/irrigation-pi/actions/workflows/pipeline.yml/badge.svg)

# Irrigation Pi
This web application turns your [Raspberry Pi](https://www.raspberrypi.com/) into an irrigation system.

There are several relay HATs vom various manufactures available for the [Raspberry Pi](https://www.raspberrypi.com/).
This application currently supports the following boards:
* [Waveshare RPi Relay Board](https://www.waveshare.com/wiki/RPi_Relay_Board) (3 relays)

Contributions for other boards are warmly welcome.

## Features
* Add schedules for switching the relays
* Relays are switched automatically according to the schedules
* [FastAPI](https://fastapi.tiangolo.com/) [backend application](backend/README.md) with self documenting REST API written in Python
* [Angular](https://angular.io/) [frontend application](frontend/README.md) written in Typescript

## Todos
The application is currently under heavy development. Current tasks/features are still to do:
* fix CORS header for frontend application
* simplify start_time format HH:MM


## Installation
[Install Poetry](https://python-poetry.org/docs/#installation) on your machine, i.e.:
```shell
curl -sSL https://install.python-poetry.org | python3 -
```

Configure poetry to install virtual environments in project folders:
```shell
poetry config virtualenvs.in-project true
```

In project root install Python package dependencies with Poetry and create a virtual environment:
```shell
poetry install
```

After creating the virtual environment you are able to use the project's management CLI.
Activate virtual environment, then install the [SQLite](https://www.sqlite.org/) database:
```shell
source .venv/bin/activate
manage install database
```

Start the backend application:
```shell
manage run backend
```
The backend application is running afterwards and is accessible on: http://0.0.0.0:8000 

Start the frontend application in another terminal:
```shell
manage run frontend
```
The frontend application is running afterwards and is accessible on: http://0.0.0.0:8100

