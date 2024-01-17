# hk_model
hk_model is a project that contains a pipeline to run a Machine Learning trained model.

<p align="left">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg"/>  
  <img src="https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white"/>
  <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"/>
</p>

![Pipeline](docs/pipeline.png)

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
bash hk_model.sh  [--output folderNameOut] [-f fileNameIn]  [--input folderNameIn] [-a arrayOfChromosomes] [-x] [--help] [--version]
```

|Parameter |Arguments|Description|
|-----------------------|-------------|-------------|
| -f | fileNameIn | The input as zip or txt file or VCF file. This parameter will overwrite the -i input parameter. |
| -i, --input  | folderNameIn | The folder name with path containing the txt.zip files to be formatted and analyzed, this only works for zipped files in a folder. 
| -o, --output | folderNameOut | The folder name with path where ancestry results will be stored. Default is the working directory. A new folder named results with a timestamp will be generated (see -s option). |
| -a | arrayOfChromosomes | Specify a subset of the 22 somatic chromosomes to be computed. An array example could be "1 2 3 4 22". Whole array must be quoted with elements separated by white spaces.  |
| -x |			  | Prevents XGMix from being executed (only prepares the data). |
| -j |		number	  | Specify the maximum number of jobs to be runned in parallel, default is set to 2. This is a parameter for "GNU parallel". | 
| -s |		stamp	  | Specify a stamp for your results folder and results files. Default is "date" e.g. results-\<YY-MM-DD--HH-MM-SS\>.| 
| --isvcf |			  | Option for specify that your input files are in vcf format (compressed). Note: currently the pipeline only supports vcf files with chromosome labels as numbers only.|
| --isphased |		  | Option to specify that the vcf is already phased. |
| -p |                | Option to select the algorithm for phasing. |
| -m |folderNameModels| Specify the path to the folder containing the models. Default is data/models/|
| -h, --help |        | Displays help. |
| --version |			  | Displays version. | 

### Examples

To run the pipeline with one sample file:
```bash
bash hk_model.sh -f input/james-007.txt.zip -o output/ -s "test"  -m data/models/
```


    
## 4. Annotated example

We have added an example to this repository that should exemplify the expected input/output files as follows:

### Input model file
A .pkl file

### Input data file
A .csv file

### Output file
A .csv file



## 5. Citation
For citation and more information refer to:

> Tripp et al (2023). DiabetIA: Building Machine Learning Models for Type 2 Diabetes Complications. MedRXiv https://doi.org/10.1101/2023.10.22.23297277


## Developers
This repository was developed and maintained by Amphora Health's scientists and engineers:

* Joaquin Tripp (joaquintripp at amphora.health)
* Daniel Santana (daniel at amphora.health)
* Arturo Lopez-Pineda, PhD (arturo at amphora.health)


## 6. Development status

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)


### Releases
- v1.0 Jan 17, 2024     	[stable] - Skywalker (Global ancestry)

 

## License
Please refer to our MIT license in this repository.

