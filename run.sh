#!/bin/bash

. ./env/bin/activate

cd $(dirname $0)
# sudo is mandatory to access GPIO
sudo python3 refresh_domoticz.py
