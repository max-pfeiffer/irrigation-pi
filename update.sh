#!/bin/bash
echo "Pulling latest main branch from GitHub..."
git checkout main
git pull

echo "Installing Python packages with Poetry..."
poetry install --sync --without dev

echo "Restarting Uvicorn server..."
poetry run irrigation-pi restart uvicorn

echo "Restarting nginx server..."
poetry run irrigation-pi restart nginx

HOSTNAME=$(hostname)
echo "Irrigation Pi application was updated and is now available on http://$HOSTNAME.local"
