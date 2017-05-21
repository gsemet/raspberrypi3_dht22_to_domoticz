#/bin/bash

echo "Setting up python environment..."
sudo apt-get update
sudo apt-get install python3 build-essential python-dev

echo
echo "Setting up requirements..."
virtualenv --python=python3 env
. ./env/bin/activate
pip install -r requirements.txt

echo "Installation complete"
echo "Edit `config.yaml` accordingly to your environment"
echo "Activate environment with $PWD/env/bin/activate"
echo "Or run directly ./run.sh"
