""" enginering.py
    This file contains the functions for data cleaning and feature enginering.
    - remove rows with all values in NaN
    - create new categorical cols
    - clean date cols

Input:
  - data/raw/hk_sample.csv
Output:
  - data/interim/hk_sample.csv
"""

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

# Import libraries
import pandas as pd
import os
import json
import pickle
from aux_01_engineering import CleanFunctions
from aux_01_engineering import CreateFunctions
from aux_01_engineering import DeleteFunctions
from aux_01_engineering import ImputeFunctions
from aux_01_engineering import ValidateFunctions
from aux_01_engineering import TransformFunctions
from references.libs.logging import logging


class DataEngineering(
    CleanFunctions,
    CreateFunctions,
    DeleteFunctions,
    ImputeFunctions,
    ValidateFunctions,
    TransformFunctions
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
        _features:list[str] = self.config['config']['features']
        
        #..Transformations starts
        self.readFile()
    
        try:

          #..validate functions
          self.validateCols()
                        
          #..create functions
          self.cleanSex()
          self.createAgeDxGroup()
          self.createAgeWxGroup()
          self.createYearSinceDx()
          self.createBmiCategory()
          self.createGlucoseCategory()
          self.createHemoglobinCategory()
          self.createTriglyceridesCategory()
          self.createGFRCategory()
          self.createCholesterolCategory()
          self.createCreatinineCategory()
          self.categoricalCols()
          self.ordinalCols()

          #..delete functions
          self.dropRows()

          #..impute functions
          self.imputeNulls()

          #..normalization
          #self.normalize()
          #self.standardize()

          logging.info('Transformations done')
          return self.data
        except Exception as e:
          logging.error(f'Transformations failed. {e}')
          raise logging.warning(f'Data was not transformed')
          
            

    def __str__(self):
        return 'Data engineering main process. It uses functions from DataEngieneeringFunctions'