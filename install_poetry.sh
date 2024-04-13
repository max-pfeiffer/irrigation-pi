#!/bin/bash
echo "Installing Poetry..."
curl -sSL https://install.python-poetry.org | python3 -

POETRY_PATH_CONFIG='export PATH="/home/admin/.local/bin:$PATH"'
BASHRC_POETRY_PATH_CONFIG=$(tail -n 1 ~/.bashrc)

if [ "$POETRY_PATH_CONFIG" != "$BASHRC_POETRY_PATH_CONFIG" ]; then
  echo $POETRY_PATH_CONFIG >> ~/.bashrc
fi

echo "Configure Poetry to create virtual environments in project directories..."
bash -c "poetry config virtualenvs.in-project true"

echo "Installing Python packages with Poetry..."
~/.local/bin/poetry install --without dev"
