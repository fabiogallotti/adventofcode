#!/usr/bin/env bash
set -euo pipefail

app="adventofcode"

docker build --pull \
  --file docker/Dockerfile \
  --tag "${app}" \
  .

docker run \
  --interactive \
  --tty \
  --rm \
  --workdir /app \
  --volume "$(pwd)":/app \
  --volume /app/.venv \
  "${app}" \
  /bin/bash
