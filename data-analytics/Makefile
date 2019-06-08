.PHONY: prepare
prepare: 
	python3.7 -m venv venv; source venv/bin/activate; pip3 install -r requirements.txt; deactivate

.PHONY: format
format:
	source venv/bin/activate; black . --exclude venv

