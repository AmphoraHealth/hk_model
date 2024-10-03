import argparse
import pandas as pd
import os
import sys
import pickle

parser = argparse.ArgumentParser(description='This script helps to run apply data engineering process requiered')
parser.add_argument('--input','-i', required=True, help='Input file name')
parser.add_argument('--output', '-o', required=False, help='Output file name')
parser.add_argument('--input-path', '-ipath', required=False, help='Specific input path')
parser.add_argument('--output-path', '-opath', required=False, help='Specific output path')
parser.add_argument('--project', '-p', required=False, help='Name of the project where model is located', default='diabetia_expert_model')
parser.add_argument('--model', '-m', required=True, help = 'Model to predict')
  

ROOT_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        os.path.pardir,
        os.path.pardir
    )
)
sys.path.append(ROOT_PATH)
from references.libs.logging import logging  


args = parser.parse_args()
INPUT:str = args.input
OUTPUT:str = args.output if args.output != None else args.input
PROJECT:str = args.project
MODEL:str = args.model

if __name__ == '__main__':
    
    # assertions
    assert os.path.exists(f'{ROOT_PATH}/data/interim/{INPUT}'), logging.error(f'Input file not exists')
    assert os.path.exists(f'{ROOT_PATH}/src/models/{PROJECT}/{MODEL}'), logging.error(f'Model not exists')
    
    # read file
    data = pd.read_csv(f'{ROOT_PATH}/data/interim/{INPUT}', low_memory=False)

    # load model
    with open(f'{ROOT_PATH}/src/models/{PROJECT}/{MODEL}', 'rb') as f:
        model = pickle.load(f)
    
    # get features
    features:list[str] = list(model.feature_names_in_)

    # make prediction
    if all([feature in data.columns for feature in features]):
        try:
            # Do predictions
            data[MODEL] = model.predict(data[features])
            probabilites = model.predict_proba(data[features]).round(6)
            prob_classes = [f'prob_class_{class_label}' for class_label in model.classes_]
            for n_class in range(len(model.classes_)):
                data[prob_classes[n_class]] = [p[n_class] for p in probabilites]
            
            results = (
                data[MODEL]
                    .value_counts()
                    .reset_index()
                    .rename(columns={'index':'Diagnostic',MODEL:'Cases'})
                    .replace(to_replace={'Diagnostic':{0.0:'Negative',1.0:'Positive'}})
            )

            # Save results
            file_name = OUTPUT.replace(".csv",f"_{MODEL.replace('.pkl','')}.csv")
            (
                data.loc[:,['id',MODEL]+prob_classes]
                    .to_csv(
                        f'{ROOT_PATH}/data/processed/{PROJECT}/{file_name}'
                        ,index=False
                    )
            )

            logging.info('Prediction done')
            logging.info(f'File saved in: {ROOT_PATH}/data/processed/')
            logging.info(f'Total:\n{"-"*72}\n{results}\n{"-"*72}')


        except Exception as e:
            logging.error(f'Error during predction: {e}')
            sys.exit()
    else:
        missing_features:list[str] = [
            feature[0] for feature in zip (
                features,
                [feature in data.columns for feature in features]
            )
        ]
        logging.error(f'Missing features:\n{missing_features}')



        