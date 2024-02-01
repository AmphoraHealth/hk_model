# Import libraries
import pandas as pd
import numpy as np
import os
import sys
from sklearn import preprocessing
from aux_01_engineering.aux_functions import snakeCase

ROOT_PATH:str = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        os.path.pardir,
        os.path.pardir,
        os.path.pardir,
        os.path.pardir,
        os.path.pardir
    )
)
sys.path.append(ROOT_PATH)
from references.libs.logging import logging


class CleanFunctions:   

    def categoricalCols(self):
        """
        Function to clean categorical columns. It is required to write in engineering_conf
        the columns which are consider as categorical. For this columns will be transformed into
        labels with LabelEnconder from sklearn. There are two types of clean:
        1. Clean categorical with non ordinal labels
        2. Clean categorical with ordinal labels
        """
        
        try:
            #..Get categorical cols from json config and encoder from sklearn
            categoricalCols:list[str] = self.config['config']['categorical_cols']
            
            ######################### Categorical non ordinal
            for col,replaces in categoricalCols.items():

                # assertion for categories
                assert all([key in replaces.keys() for key in self.data[col].unique()]), logging.info(f"Categories in {col} must be {list(replaces.keys())}")
                self.data.loc[:,col] = self.data.loc[:,col].replace(to_replace=replaces)

            ######################### Categorical ordinal
            for measure in self.config['categoricalMeasuresConfig'].items():
                labels:list[str] = measure[1]['labels']

                categories:dict = {
                    category:index for index, category in enumerate(labels)
                }

                #..inserting new col
                col_index:int = self.data.columns.get_loc(measure[1]['labelCol'])
                self.data.insert(col_index+1,measure[1]['ordinalCol'],np.nan)
                self.data[measure[1]['ordinalCol']] = self.data[measure[1]['labelCol']].map(categories)
                
                
            return logging.info('Categorical cols transformed')
        
        except Exception as e:
            raise logging.error(f'{self.categoricalCols.__name__} failed. {e}')
        

    def ordinalCols(self):
        """
        Function to clean ordinal columns. It is required to write in engineering_conf
        the columns which are consider as ordinal. 
        """
        try:
            #..Get ordinal cols from json config file
            ordinalCols:list[str] = self.config['config']['ordinal_cols']

            #..Loop all columns in config
            for column in ordinalCols:
                self.data[column] = \
                    pd.to_datetime(self.data[column], errors='coerce', dayfirst=True)\
                    .apply(lambda x: x.toordinal() if pd.isnull(x) == False else x)
                
            return logging.info('Ordinal cols transformed')
        except Exception as e:
            raise logging.error(f'{self.ordinalCols.__name__} failed. {e}') 
