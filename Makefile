model:= ./src/models/model1/EXPERT_E112.pkl
file:= ./data/raw/example.csv

create_env:
	bash run_enviroment.sh

run_model: create_env
	bash mlruns.sh

