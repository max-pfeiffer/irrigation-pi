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

![ui_schedule_list.png](ui_schedule_list.png)   ![ui_schedule_detail.png](ui_schedule_detail.png)

## Features
* Add schedules for switching the relays
* Relays are switched automatically according to schedule configuration
* Mobile friendly web interface ([Angular](https://angular.io/) [frontend application](frontend/README.md) written in Typescript)
* REST API ([FastAPI](https://fastapi.tiangolo.com/) [backend application](backend/README.md) written in Python)

## Installation on Raspberry Pi
The installation on your Raspberry Pi is quickly done within minutes.

Open a shell on your Raspberry Pi and [install Poetry](https://python-poetry.org/docs/#installation):
```shell
curl -sSL https://install.python-poetry.org | python3 -
```

Configure poetry to install virtual environments in project folders:
```shell
poetry config virtualenvs.in-project true
```

Go to the directory where you want to install the application. Pull the repository:
```shell
git pull https://github.com/max-pfeiffer/irrigation-pi.git
```

In project root install Python package dependencies with Poetry and create a virtual environment:
```shell
cd irrigation-pi
poetry install
```

Activate the virtual environment. Then install application dependencies and configuration files for irrigation-pi
application, nginx and systemd using the management CLI:
```shell
source .venv/bin/activate
irrigation-pi install all
```
The management CLI requires superuser privileges for installation. If you encounter a password challenge, please enter your user's
password.

The application is available on http://raspberrypi.local/ afterwards. The API can also be used directly
on http://raspberrypi.local/api.


## Installation for Development
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
irrigation-pi install database
```

Start the backend application:
```shell
irrigation-pi run backend
```
The backend application is running afterwards and is accessible on: http://0.0.0.0:8000/api 

After environment and development setup for [frontend application](frontend/README.md), you can start the frontend application in another terminal:
```shell
irrigation-pi run frontend
```
The frontend application is running afterwards and is accessible on: http://0.0.0.0:8100

## Roadmap
Following features are on our todo list:
* Make host name for Raspberry Pi installation configurable
* Validate schedules to avoid collisions
* View for live relay switching
* View for Raspberry Pi system information
