#!/bin/bash
echo "Pulling latest main branch from GitHub..."
git checkout main
git pull

echo "Installing Python packages with Poetry..."
poetry install --sync --without dev

poetry run irrigation-pi restart uvicorn
poetry run irrigation-pi restart nginx
