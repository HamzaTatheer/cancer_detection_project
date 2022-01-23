#!/bin/sh
apt update
apt install -y openslide-tools
pip3 install git+https://github.com/ysbecca/py-wsi
pip3 install pandas
cd /shared_local/pmnet/pmnet_code
python3 ./convert_bach_to_patches.py
