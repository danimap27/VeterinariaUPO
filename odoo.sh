#!/bin/bash

cd ..
cd ..
docker compose stop
docker compose up -d
xdg-open "http://localhost:28069/web/"
