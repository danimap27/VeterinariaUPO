#!/bin/bash

ORIGEN="/home/dani/odoo/addons/VeterinariaUPO"
DESTINO="/home/dani/odooBeta/addons/VeterinariaUPO"

if [ -d "$ORIGEN" ]; then
    if [ -d "$DESTINO" ]; then
        rm -r "$DESTINO"
    fi

    # Copiar la carpeta de origen a la carpeta de destino
    cp -r "$ORIGEN" "$DESTINO"

    echo "La carpeta VeterinariaUPO se ha copiado y reemplazado en $DESTINO."
else
    echo "La carpeta de origen $ORIGEN no existe."
fi
