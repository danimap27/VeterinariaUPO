#!/bin/bash
<<<<<<< HEAD

docker compose stop

#!/bin/bash

=======
cd ..
cd ..
docker compose stop

>>>>>>> 9dadd20 (atributos de la clase persona declarados)
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
<<<<<<< HEAD


echo "Operaciones completadas."

=======
if 

sudo systemctl restart docker

echo "Operaciones completadas."
cd ..
cd ..
>>>>>>> 9dadd20 (atributos de la clase persona declarados)
docker compose up -d
