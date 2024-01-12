#!/bin/bash

env_name="venv"
python_version="3.9"

# validate enviroment
if [ -d "$env_name" ]; 
then
    rm -rf "$env_name"
fi

# validate python version
if [ -x "$(command -v python3)" ];
then
    echo -e "\033[34m>>> $(python3 -V) is installed\033[0m"
else 
    echo -e "\033[31mERROR >>> Python3 is required to continue\033[0m"
    echo -e "\033[33mWARNING >>> INSTALL python 3.9 (recommended) and run again run_enviroment.sh\033[0m"
    exit 1
fi

# create venv
virtualenv $env_name --python=$python_version
if [ ! -d "$env_name"];
then
    echo -e "\033[31mERROR >>> $env_name not created\033[0m"
    exit1
fi

# install requirements.txt
source $env_name/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
errors=$?
deactivate

if [ $errors -eq 0 ];
then
    echo -e "\033[34m>>> requirements installed\033[0m"
    echo -e "\033[34m>>> virtual enviroment created successfully\033[0m"
else
    echo -e "\033[31mERROR >>> requirements.txt installation failed\033[0m"
fi




