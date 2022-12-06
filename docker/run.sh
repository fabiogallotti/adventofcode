set -e
app="adventofcode"
docker build -t ${app} ./docker/
docker run -it --rm -w /app -v $(pwd):/app ${app} /bin/bash
