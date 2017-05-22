#/bin/bash

echo "Setting up python environment..."
sudo apt-get update
sudo apt-get install -y python3 \
                        build-essential \
                        python3-dev \
                        python3-virtualenv

echo
echo "Setting up Python environment..."
rm -rfv env/
virtualenv --python=python3 env
. ./env/bin/activate
pip install -r requirements.txt

echo
echo "Installation complete"
echo "Edit `config.yaml` accordingly to your environment"
echo "Activate environment with $PWD/env/bin/activate"
echo "Or run directly ./run.sh"
