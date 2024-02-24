#!/bin/bash
echo "Installing Poetry..."
curl -sSL https://install.python-poetry.org | python3 -
echo 'export PATH="/home/admin/.local/bin:$PATH"' >> ~/.bashrc

echo "Configure Poetry to create virtual environments in project directories..."
bash -c "poetry config virtualenvs.in-project true"

echo "Installing Python packages with Poetry..."
bash -c "poetry install --without dev"
