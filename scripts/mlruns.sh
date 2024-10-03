#!/bin/bash

FILE=$1
MODEL=$2
PROJECT=$3

# run python3 model
python3 src/models/run_model.py -i $FILE -m $MODEL -p $PROJECT


