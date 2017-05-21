#!/bin/bash

. ./env/bin/activate

cd $(dirname $0)
python3 refresh_domoticz.py
