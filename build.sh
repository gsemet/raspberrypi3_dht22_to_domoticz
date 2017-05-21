#/bin/bash

sudo apt-get update
sudo apt-get install build-essential python-dev

virtualenv --python=python3 env
. ./env/bin/activate
pip install -r requirements.txt

echo "Activate environment with env/bin/activate"
