#!/bin/bash

docker build -t demo-agent .
docker run --rm -it --name=demo-agent --device=/dev/input/js0 --net=host demo-agent
