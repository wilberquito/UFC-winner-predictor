#!/bin/bash

##  build jupyterlab image
cd lab/
docker build --no-cache -t jupyterlab:latest .

## build postgreslab image
cd ../
cd postgres/
docker build --no-cache -t postgreslab:latest .

## execute docker compose
cd ../
docker compose up

