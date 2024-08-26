""" run_preprocess.py
    This file run the preprocess for diabetia_expert_model
  
Input:
  - data/raw/hk_sample.csv
Output:
  - data/interim/hk_sample.csv
"""

import argparse
import sys
import os
ROOT_PATH:str = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        os.path.pardir,
        os.path.pardir,
        os.path.pardir
    )
)
FILE_PATH:str = os.path.dirname(__file__)
sys.path.append(ROOT_PATH)
sys.path.append(f'{FILE_PATH}/diabetia_expert_model')

parser = argparse.ArgumentParser(description='This script helps to run data engineering process requiered')
parser.add_argument('--input','-i', required=True, help='Input file name')
parser.add_argument('--output', '-o', required=False, help='Output file name', default='unknown.csv')
parser.add_argument('--inpath', '-ipath', required=False, help='Specific input path', default=f'{ROOT_PATH}/data/raw')
parser.add_argument('--outpath', '-opath', required=False, help='Specific output path', default=f'{ROOT_PATH}/data/interim')
parser.add_argument('--project', '-p', required=False, help='Name of the project where model is located', default='diabetia_expert_model')
args = parser.parse_args()

# Constants
INPUT = args.input
OUTPUT = args.output if args.output != 'unknown.csv' else args.input
IN_PATH = f'{args.inpath}/{INPUT}'
OUT_PATH = f'{args.outpath}/{OUTPUT}'
PROJECT = args.project
CONFIG_PATH = f'{ROOT_PATH}/config/{PROJECT}/engineering_conf.json'

# Import libraries
import pandas as pd
import os
import json
from references.libs.logging import logging
from diabetia_expert_model import DataEngineering

_preprocess:dict[str:object] = {
    "diabetia_expert_model":DataEngineering
}

def runDataEngineering() -> pd.DataFrame:
    """
    Function to run all data engineering process
    """
    # intialize class
    try:
      _DataEngineering =  _preprocess[PROJECT]
      data_engineering = _DataEngineering(
          IN_PATH=IN_PATH,
          CONFIG_PATH=CONFIG_PATH
      )

      # Run transformations
      data = data_engineering.mainTransform()

      # Save file
      data.to_csv(f'{OUT_PATH}', index=False, encoding='UTF-8')
      
      return logging.info(f'File saved on {OUT_PATH}')
    
    except Exception as e:
        logging.error(f'{runDataEngineering.__name__} process failed. {e}')
        sys.exit()


if __name__ == '__main__':
    runDataEngineering()