#!/bin/bash

CONTAINER_NAME="odooBeta"
FOLDER="/usr/lib/python3/dist-packages/odoo/addons/"

docker exec -it $CONTAINER_NAME find $FOLDER -name '*.py'
