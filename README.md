# hk_model: Streamlined Machine Learning Deployment

The `hk_model` project offers a pipeline for efficiently deploying and running trained machine learning models. Designed to streamline the process from model training to deployment, this tool is a vital asset for data scientists and ML engineers.

![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![scikit_learn](https://img.shields.io/badge/scikit_learn-F7931E.svg?style=flat&logo=scikit-learn&logoColor=white)
![Python](https://img.shields.io/badge/Python-FFD43B.svg?style=flat&logo=python&logoColor=blue)
![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)


![Pipeline Image](docs/pipeline.png)

Click on the image below to watch the demo video:

[![Demo Video](https://img.youtube.com/vi/Ycl_yTK0Dig/0.jpg)](https://www.youtube.com/watch?v=Ycl_yTK0Dig)



## 1. Description
**Amphora Health's hk_model**: A Biomedical ML Pipeline. Our `hk_model` effortlessly evaluates trained biomedical machine learning models against new patient datasets. Discover a curated collection of pre-trained models in our `models` folder, ready for diverse medical data analysis applications.

## 2. Installation

### Folder Structure
Organized and intuitive, the `hk_model` project structure is as follows:

    
    ├── config/
		└── diabetia_expert_model
	     		├── requirements.txt
	      		└── run_enviroment.sh
    ├── data/
    ├── docs/
    ├── references/
    ├── scripts/
		├── ml_runs.sh/
		└── preprocess.sh/
    ├── src
		├── data/
		├── features/
		├── models/
			└── run_model.py
		└── visualizations/
    ├── .gitignore
    ├── docker-compose.yml
    ├── Dockerfile
    ├── LICENSE
    ├── Makefile
    └── README.md
    
    
This project uses Docker to manage its environment and dependencies, ensuring consistency across different systems. Follow the steps below to build and run the project using Docker.

### Prerequisites
- Ensure you have Docker installed on your system.


## 3. Build the Docker Image
To run this **hk_model** Pipeline, you will need to be in the top level folder and then build the Docker image, run the following command:

```bash
docker build -t diabetia:v1.0 .
```
## 4. Running the Docker container
After building the image, you can start the container using the following command:

```bash
FILE=hk_sample.csv MODEL=gaussian_e112.pkl docker compose up inference
```

#### Parameters Explained
Understand each parameter for a successful execution:

| Parameter | Argument         | Description |
|-----------|------------------|-------------|
| `FILE`    | `<input_file_name>` | Name of the input file located in `data/raw/`. This file should contain new instances for prediction. |
| `MODEL`   | `<model_name>`   | Name of the pre-trained model for predictions, found in `src/models/`. |


## 4. Citation
For academic referencing, please cite our work as follows:

> Tripp et al. (2023). "DiabetIA: Building Machine Learning Models for Type 2 Diabetes Complications." MedRXiv. [DOI](https://doi.org/10.1101/2023.10.22.23297277).



## 5. Development Status

### Developers
The `hk_model` repository is a product of Amphora Health's team:

- Joaquin Tripp - *Data Science Manager*  
  📧 joaquintripp [at] amphora.health

- Daniel Santana - *Data Scientist*  
  📧 daniel [at] amphora.health


### Current Release
- **Version 1.1.0**  
  Released on Oct 3, 2024  
  Status: 🟢 Stable Release


 

## 6. License
Please refer to our MIT license in this repository.

