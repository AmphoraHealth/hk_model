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
    )
)
sys.path.append(ROOT_PATH)
from references.libs.logging import logging


class ImputeFunctions:

    def imputeNulls(self):
        """
        Function to impute nulls in numerical variables. It is requiered to apply 
        previous data engineering process before impute, because some variables target
        are created in create.py. To the imputation there is only one case:
        1. Null values
        """
        targetCols:list[str] = [
            'bmi_value',
            'bmi_ordinal',
            'diabetes_mellitus_type_2', 
            'essential_(primary)_hypertension',
            'disorders_of_lipoprotein_metabolism_and_other_lipidemias',
            'gfr_value',
            'gfr_ordinal',
            'glucose_value',
            'glucose_ordinal',
            'hemoglobin_value',
            'hemoglobin_ordinal', 
            'triglycerides_value',
            'triglycerides_ordinal',
            'cholesterol_value',
            'cholesterol_ordinal'
        ]
        try:
            # fill with 0 in case of nulls
            self.data.loc[:,targetCols] = self.data.loc[:,targetCols].fillna(0)
            return logging.info(f'Nulls imputed')
        except Exception as e:
            raise logging.error(f'{self.imputeNulls.__name__} failed. {e}')