#!/bin/bash
set -e

echo "Pulling latest main branch from GitHub..."
git checkout main
git pull

echo "Installing Python packages with Poetry..."
~/.local/bin/poetry install --sync --without dev

echo "Restarting Uvicorn server..."
~/.local/bin/poetry run irrigation-pi restart uvicorn

echo "Restarting nginx server..."
~/.local/bin/poetry run irrigation-pi restart nginx

HOSTNAME=$(hostname)
echo "Irrigation Pi application was updated and is now available on http://$HOSTNAME.local"
