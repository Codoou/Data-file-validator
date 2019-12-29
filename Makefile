all: run

clean:
	rm -rf venv && rm -rf *.egg-info && rm -rf dist && rm -rf *.log*

venv:
	python3 -m venv venv && venv/bin/python setup.py develop

run: venv
	FLASK_APP=data_file_validator DATA_FILE_VALIDATOR_SETTINGS=../settings.cfg venv/bin/flask run

test: venv
	DATA_FILE_VALIDATOR_SETTINGS=../settings.cfg venv/bin/python -m unittest discover -s tests

sdist: venv test
	venv/bin/python setup.py sdist
