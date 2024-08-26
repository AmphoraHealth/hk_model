# Import libraries
import pandas as pd
import numpy as np
import os
import sys
import pickle
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
PROJECT:str = 'diabetia_expert_model'


class TransformFunctions:

    def normalize(self):
        """
        Function to normalize columns specified in engineering_conf. It is required
        to have all necessary columns to process. Yeo-Johnson method was selected
        to normalize data.
        """

        try:
            #.. Get columns to normalize
            normalizeCols:list[str] = self.config['columns_to_standardize']['normalize']

            #.. Get normalizer
            norm_method = self.config["columns_to_standardize"]["methods"]["normalizer"]
            with open(f'{ROOT_PATH}/src/models/diabetia_expert_model/standardizers/{norm_method}','rb') as f:
                normalizer = pickle.load(f)
        

            #.. normalize columns
            self.data.loc[:,normalizeCols] = normalizer.transform(self.data.loc[:,normalizeCols])

            return logging.info(f'Columns normalized by {norm_method}')

        except Exception as e:
            raise logging.error(f'{self.normalize.__name__} failed.{e}')
        
    
    def standardize(self):
        """
        Function to standardize columns specified in engineering_conf. It is required
        to have all necessary columns to process. Z-score method was selected
        to standardize data.
        """

        try:
            #.. Get columns to normalize
            standardizeCols:list[str] = self.config['columns_to_standardize']['standardize']

            #.. Get normalizer
            standardize_method = self.config["columns_to_standardize"]["methods"]["standardizer"]
            with open(f'{ROOT_PATH}/src/models/diabetia_expert_model/standardizers/{standardize_method}','rb') as f:
                normalizer = pickle.load(f)
        

            #.. standardize columns
            self.data.loc[:,standardizeCols] = normalizer.transform(self.data.loc[:,standardizeCols])

            return logging.info(f'Columns normalized by {standardize_method}')

        except Exception as e:
            raise logging.error(f'{self.standardize.__name__} failed.{e}')