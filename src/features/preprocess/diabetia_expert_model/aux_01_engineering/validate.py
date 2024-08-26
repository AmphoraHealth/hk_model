# Import libraries
import pandas as pd
import os
import sys

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
from references.libs.logging import logging

class ValidateFunctions:

    def validateCols(self):
        """
        Function to validate values in specific columns
        """
        
        _features:list[str] = self.config['config']['features']
        _missing_features:list[str] = [feature for feature in _features if feature not in self.data.columns]
        _categoricalCols:list[str] = self.config['config']['categorical_cols']

        assert all([feature in self.data.columns for feature in _features]),\
            logging.error(f'Missing features:\n{_missing_features}')

        for col,replaces in _categoricalCols.items():
            if col=='cs_sex':
                continue
            else:
                assert \
                    all(
                        [
                            key in replaces.keys() for key in self.data[col].unique()
                        ]
                    ),\
                    logging.error(f"Categories in {col} must be {list(replaces.keys())}")
            
        
        assert self.data['id'].nunique() == self.data.shape[0],\
            logging.error("IDs must be uniques")

        