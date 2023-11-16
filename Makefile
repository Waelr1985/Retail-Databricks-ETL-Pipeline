install:
	pip install --upgrade pip && pip install -r requirements.txt

format:
	black *.py 

deploy:
	# Deploy goes here

all: install format deploy

job:
	python run_job.py
