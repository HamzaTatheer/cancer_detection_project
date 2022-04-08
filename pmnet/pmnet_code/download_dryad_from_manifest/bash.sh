#!/bin/sh
pip3 install docopt
cd /shared/pmnet/
python3 ./pmnet_code/download_dryad_from_manifest/download_dryad_from_manifest.py -f ./pmnet_dataset/dryad/manifest_1_173.txt -d ./pmnet_dataset/dryad/WSI/
