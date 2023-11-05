#!/bin/bash

echo "Limpiando volúmenes Docker no utilizados..."
docker volume prune -f

echo "Limpiando imágenes Docker no utilizadas..."
docker image prune -af

echo "Limpiando contenedores Docker detenidos..."
docker container prune -f

echo "Reiniciando el servicio Docker..."
sudo systemctl restart docker

echo "Operaciones completadas."

docker compose up -d
