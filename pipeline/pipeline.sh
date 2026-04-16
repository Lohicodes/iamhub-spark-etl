#!/bin/bash

echo "step1: Building docker image..."
docker build -t spark-local -f docker/Dockerfile .

echo "step2: Running spark job in docker container..."
docker run --rm spark-local \
  --input /data/input/sample.csv \
  --output /data/output/processed_data.csv

echo "pipeline completed. Processed data is available at data/output/processed_data.csv"