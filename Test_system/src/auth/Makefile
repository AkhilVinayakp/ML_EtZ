# Makefile
SHELL := /bin/bash

SAMPLE_DATA_FILE=sample_data.py
SERVER=server.py

dev_setup:
	@echo "setting up local dev environment"

setup: dev_setup
	@echo "Setting up the environment for app"
	@source setup.sh

sample_insert:
	@echo "inserting sample documents in the db."
	@source setup.sh && python3 $(SAMPLE_DATA_FILE)

run_server:
	@echo "Starting the server."
	@source setup.sh && python3 $(SERVER)