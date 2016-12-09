#!/usr/bin/env bash
virtualenv -p python3 entorno
source entorno/bin/activate

pip install -r ./requirements.txt
