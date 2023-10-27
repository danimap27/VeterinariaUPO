#!/bin/bash

<<<<<<< HEAD
ORIGEN="/home/dani/odoo/addons/VeterinariaUPO"
DESTINO="/home/dani/odooBeta/addons/VeterinariaUPO"
=======
ORIGEN="/home/dani/odooBeta/addons/VeterinariaUPO"
DESTINO="/home/dani/odoo/addons/VeterinariaUPO"
>>>>>>> 9dadd20 (atributos de la clase persona declarados)

if [ -d "$ORIGEN" ]; then
    if [ -d "$DESTINO" ]; then
        rm -r "$DESTINO"
    fi

<<<<<<< HEAD
    # Copiar la carpeta de origen a la carpeta de destino
=======
>>>>>>> 9dadd20 (atributos de la clase persona declarados)
    cp -r "$ORIGEN" "$DESTINO"

    echo "La carpeta VeterinariaUPO se ha copiado y reemplazado en $DESTINO."
else
    echo "La carpeta de origen $ORIGEN no existe."
fi
