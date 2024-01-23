#!/bin/bash

FILE=$1
PROJECT=$2

# activate enviroment
source venv/bin/activate

# run python3 model
python3 src/features/preprocess/run_preprocess.py -i $FILE -p $PROJECT

# deactivate
deactivate


