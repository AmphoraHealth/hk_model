#!/bin/bash

FILE=$1
PROJECT=$2

# run python3 model
python3 src/features/preprocess/run_preprocess.py -i $FILE -p $PROJECT



