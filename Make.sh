#!/bin/bash

##  build jupyterlab image
cd lab/
docker build -t jupyterlab:latest .

## build postgreslab image
cd ../
cd postgres/
docker build -t postgreslab:latest .

## execute docker compose
cd ../
docker compose up

