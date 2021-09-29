#!/bin/bash
cd .. && \
docker build --rm -t local/simple-api:v0.1 -f 2/Dockerfile .