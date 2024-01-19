VENV := venv
VENV_CREATED := $(WILDCARD $(VENV))
MODEL ?= gaussian_e112.pkl
FILE ?= hk_sample.csv
PROJECT ?= diabetia_expert_model

run_model: data/interim/$(FILE)
	@echo "\033[1;34mRUNNING PREDICTION OF $(MODEL) MODEL\033[0m"
	@bash ./scripts/mlruns.sh $(FILE) $(MODEL) $(PROJECT)

data/interim/$(FILE): venv/bin/activate
	@echo "\033[1;34mRUNNING FILE PREPROCESS\033[0m"
	@python3 src/features/preprocess/$(PROJECT)/data_engineering.py -i $(FILE)

venv/bin/activate: $(VENV_CREATED)
	@echo "\033[1;31mENVIROMENT NOT FOUND\033[0m"
	@echo "\033[1;34mINSTALLING ENVIROMENT\033[0m"
	@bash ./config/run_enviroment.sh