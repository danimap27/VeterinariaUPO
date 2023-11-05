#!/bin/bash

cd ..
cd ..
docker compose stop

echo "Limpiando volúmenes Docker no utilizados..."
docker volume prune -f

echo "Limpiando imágenes Docker no utilizadas..."
docker image prune -af

echo "Limpiando contenedores Docker detenidos..."
docker container prune -f
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker system prune -a

echo "Reiniciando el servicio Docker..."
sudo systemctl restart docker


echo "Operaciones completadas."
sudo systemctl restart docker

echo "Operaciones completadas."
cd ..
cd ..
docker compose up -d
