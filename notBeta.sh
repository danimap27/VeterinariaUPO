#!/bin/bash

carpeta_a_reemplazar="VeterinariaUPO"
usuario_actual=$(whoami)
ruta_base_usuario="/home/$usuario_actual"

carpeta_origen="$ruta_base_usuario/$1/odooBeta/addons/$carpeta_a_reemplazar"

carpeta_destino="$ruta_base_usuario/$2/odoo/addons/$carpeta_a_reemplazar"

if [ -d "$carpeta_origen" ]; then
  if [ -d "$carpeta_destino" ]; then
    # Cambiar al directorio de origen
    cd "$ruta_base_usuario/$1/odoo/addons/"
    rsync -av --delete "$carpeta_a_reemplazar" "$ruta_base_usuario/$2/odoo/addons/"
    echo "La carpeta '$carpeta_a_reemplazar' en '$2' ha sido reemplazada por la carpeta de origen."
  else
    echo "La carpeta de destino '$carpeta_destino' no existe."
  fi
else
  echo "La carpeta de origen '$carpeta_origen' no existe."
fi

