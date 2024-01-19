""" enginering.py
    This file contains the functions for data cleaning and feature enginering.
    - remove unnecessary columns
    - one-hot encoding (if needed)

Input:
  - data/hk_database.csv
Output:
  - data/hk_database_cleaned.csv
Additional outputs:
  - None
"""
import argparse
import sys
import os
ROOT_PATH:str = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        os.path.pardir,
        os.path.pardir,
        os.path.pardir,
        os.path.pardir
    )
)
sys.path.append(ROOT_PATH)

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
from aux_01_engineering import CleanFunctions
from aux_01_engineering import CreateFunctions
from aux_01_engineering import DeleteFunctions
from aux_01_engineering import ImputeFunctions
from references.libs.logging import logging


class DataEngineering(
    CleanFunctions,
    CreateFunctions,
    DeleteFunctions,
    ImputeFunctions
    ):
    
    def __init__(
        self,
        IN_PATH:str,
        CONFIG_PATH:str
      ):
        self.in_path:str = IN_PATH
        self.config_path:str = CONFIG_PATH
        self.data:pd.DataFrame = pd.DataFrame()
        self.config:dict = json.load(open(f'{self.config_path}', 'r', encoding='UTF-8'))
    
    def readFile(self,rows:int = None):
        try:
            self.data = pd.read_csv(f'{self.in_path}', low_memory=False, nrows=rows)
            return logging.info('File read')
        except Exception as e:
            raise logging.error(f'File was not read. {e}')
        

    def mainTransform(self) -> pd.DataFrame:
        """
        Function to run all transformations.
        """
        try:
          #..Transformations starts
          self.readFile()

          #..create functions
          self.createAgeDxGroup()
          self.createAgeWxGroup()
          self.createYearSinceDx()
          self.createBmiCategory()
          self.createGlucoseCategory()
          self.createHemoglobinCategory()
          self.createTriglyceridesCategory()
          self.createGFRCategory()
          self.createCholesterolCategory()
          self.categoricalCols()
          self.ordinalCols()

          #..delete functions
          # self.dropCols()
          self.dropRows()

          #..impute functions
          self.imputeNulls()

          logging.info('Transformations done')
          return self.data
        except Exception as e:
            raise logging.error(f'Transformations failed. {e}')
            

    def __str__(self):
        return 'Data engineering main process. It uses functions from DataEngieneeringFunctions'


def runDataEngineering() -> pd.DataFrame:
    """
    Function to run all data engineering process
    """
    # intialize class
    try:
      data_engineering = DataEngineering(
          IN_PATH=IN_PATH,
          CONFIG_PATH=CONFIG_PATH
      )

      # Run transformations
      data = data_engineering.mainTransform()

      # Save file
      data.to_csv(f'{OUT_PATH}', index=False, encoding='UTF-8')
      
      return logging.info(f'File saved on {OUT_PATH}')
    
    except Exception as e:
        raise logging.error(f'{runDataEngineering.__name__} process failed. {e}')


if __name__ == '__main__':
    logging.info(f'{"="*30}DATA ENGINEERING STARTS')
    runDataEngineering()
    logging.info(f'{"="*30}DATA ENGINEERING FINISHED')