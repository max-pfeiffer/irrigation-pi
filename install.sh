#!/bin/bash
set -e

echo "Installing dependencies for building Python packages..."
apt-get update
apt-get install --no-install-recommends -y build-essential python3-dev

echo "Installing uv..."
curl -LsSf https://astral.sh/uv/install.sh | sh

UV_PATH_CONFIG='export PATH="$HOME/.local/bin:$PATH"'
BASHRC_UV_PATH_CONFIG=$(tail -n 1 ~/.bashrc)

if [ "$UV_PATH_CONFIG" != "$BASHRC_UV_PATH_CONFIG" ]; then
  echo $UV_PATH_CONFIG >> ~/.bashrc
fi

echo "Installing Python packages with uv..."
~/.local/bin/uv sync --no-dev

echo "Installing Debian packages and configure application..."
~/.local/bin/uv run irrigation-pi install all

HOSTNAME=$(hostname)
echo "Irrigation Pi application is now available on http://$HOSTNAME.local"
