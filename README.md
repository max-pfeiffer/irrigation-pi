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
* Relays are switches automatically according to the schedules
* Backend application with REST API
* Frontend: coming soon

## Installation
[Install Poetry](https://python-poetry.org/docs/#installation) on your machine, i.e.:
```shell
curl -sSL https://install.python-poetry.org | python3 -
```

Configure poetry to install virtual environments in project folders:
```shell
poetry config virtualenvs.in-project true
```

In project root install Python package dependencies with Poetry:
```shell
poetry install
```

Now you are able to use the projects management CLI after activating the virtual environment.
Activate virtual environment, then install backend dependencies and database:
```shell
source .venv/bin/activate
manage install backend-dependencies
manage install backend-database
```

Start the backend application:
```shell
manage run backend
```

The backend application is running afterwards and is accessible on: http://0.0.0.0:8000 
