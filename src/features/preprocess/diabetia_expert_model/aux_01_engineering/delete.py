# Import libraries
import pandas as pd
import os
import sys
import re

ROOT_PATH:str = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        os.path.pardir,
        os.path.pardir,
        os.path.pardir,
        os.path.pardir,
    )
)
sys.path.append(ROOT_PATH)
from references.libs.logging import logging

class DeleteFunctions:
    def dropCols(self):
        """
        Function to drop next columns:
        - unnecesary columns or informative
        """   
        try:
            #..Drop unncessesary columns by json file
            dropUnnecessaryCols:list[str] = self.config['config']['columnsToDrop']['unnecessaryCols']
            self.data.drop(columns=dropUnnecessaryCols, inplace=True)

            columnsDropped:int = len(dropUnnecessaryCols)
            
            return logging.info(f'{columnsDropped} columns dropped')
        
        except Exception as e:
            raise logging.error(f'{self.dropCols.__name__} failed. {e}')


    def dropRows(self):
        """
        Function to drop rows: 
        - where some measure is null
        """
        _requeried_columns:list = [
            "cs_sex",
            "birthdate",
            "years_since_dx",
            "age_at_wx",
            "dx_age_e11"
        ]
        try:
            #..drop rows without data in principal variables.
            intialRows:int = self.data.shape[0] 
            self.data = self.data.loc[
                (self.data[_requeried_columns].isnull().sum(axis=1) == 0),:
            ]

            logging.info(f'{intialRows-self.data.shape[0]} rows dropped.')
        except Exception as e:
            raise logging.error(f'{self.dropRows.__name__} failed. {e}')