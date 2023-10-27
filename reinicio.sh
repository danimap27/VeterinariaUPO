#!/bin/bash

docker compose stop

<<<<<<< HEAD
#!/bin/bash

=======
>>>>>>> 9dadd20 (atributos de la clase persona declarados)
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
