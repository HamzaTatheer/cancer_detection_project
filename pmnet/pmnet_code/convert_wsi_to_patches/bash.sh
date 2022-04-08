#!/bin/sh
apt update
apt install -y openslide-tools
pip3 install git+https://github.com/ysbecca/py-wsi
pip3 install pandas
cd /shared/pmnet/pmnet_code/convert_wsi_to_patches
python3 ./convert_wsi_to_patches.py
