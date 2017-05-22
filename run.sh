#!/bin/bash

# Run this script as 'root' user (mandatory to access to GPIO)
if [[ -z $VIRTUAL_ENV ]]; then
    . ./env/bin/activate
fi

cd $(dirname $0)
python3 refresh_domoticz.py
