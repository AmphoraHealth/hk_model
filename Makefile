VENV := venv
VENV_CREATED := $(WILDCARD $(VENV))
MODEL ?= gaussian_e112.pkl
FILE ?= hk_sample.csv
PROJECT ?= diabetia_expert_model

run_model: data/interim/$(FILE)
	@echo "\033[1;34mRUNNING PREDICTION OF $(MODEL) MODEL\033[0m"
	@bash ./scripts/mlruns.sh $(FILE) $(MODEL) $(PROJECT)

data/interim/$(FILE): 
	@echo "\033[1;34mRUNNING FILE PREPROCESS\033[0m"
	@bash ./scripts/preprocess.sh $(FILE) $(PROJECT)