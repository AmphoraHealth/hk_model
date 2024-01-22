# hk_model
hk_model is a project that contains a pipeline to run a Machine Learning trained model.

<p align="left">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg"/>  
  <img src="https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white"/>
  <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"/>
</p>

Click on the image below to watch the demo video:

<iframe width="500" height="300" src="https://www.youtube.com/embed/Ycl_yTK0Dig>" frameborder="0" allowfullscreen></iframe>



## 1. Description
The Amphora Health **hk_model** pipeline takes a trained biomedical machine learning model and evaluates it agains new patient datasets. You can find a list of pre-trained models in our models folder.


## 2. Instalation

### Folder structure

    .
    ├── docs/
    ├── data/
    ├── engineering/
	├── env/
	├── models/
    ├── main.sh
    ├── requirements.txt
    └── README.md



### Prerrequisites

For a full list of requirements and prerrequisites please see the `requirements.txt` file


## 3. Usage
To run this **hk_model** Pipeline, you will need to be in the top level folder and then execute the following command to be run in Unix (Mac):

```bash
make run_model FILE=fileNameIn MODEL=modelName
```

|Parameter |Arguments|Description|
|-----------------------|-------------|-------------|
| FILE | fileNameIn | The input file name in the data/raw/ subfolder that contains the new instances to be predicted |
| MODEL  | modelName | The trained model to be used in the predictions that are available in src/models/ 

### Examples

To run the pipeline with one sample file:
```bash
make run_model FILE=hk_sample.csv MODEL=gaussian_e112.pkl
```


## 4. Citation
For citation and more information refer to:

> Tripp et al (2023). DiabetIA: Building Machine Learning Models for Type 2 Diabetes Complications. MedRXiv https://doi.org/10.1101/2023.10.22.23297277


## Developers
This repository was developed and maintained by Amphora Health's scientists and engineers:

* Joaquin Tripp (joaquintripp at amphora.health)
* Daniel Santana (daniel at amphora.health)
* Arturo Lopez-Pineda, PhD (arturo at amphora.health)


## 5. Development status

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)


### Releases
- v1.0 Jan 17, 2024     	[stable] 

 

## License
Please refer to our MIT license in this repository.

