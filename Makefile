install:
	pip install --upgrade pip && pip install -r requirements.txt

format:
	black *.py 

lint:
	#Lint goes here

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

deploy:
	# Deploy goes here

all: install format deploy

job:
	python run_job.py
