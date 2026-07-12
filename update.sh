#!/bin/bash
set -e

echo "Pulling latest main branch from GitHub..."
git checkout main
git pull

echo "Installing Python packages with uv..."
~/.local/bin/uv sync --no-dev

echo "Restarting Uvicorn server..."
~/.local/bin/uv run irrigation-pi restart uvicorn

echo "Restarting nginx server..."
~/.local/bin/uv run irrigation-pi restart nginx

HOSTNAME=$(hostname)
echo "Irrigation Pi application was updated and is now available on http://$HOSTNAME.local"
