.PHONY: prepare
prepare: 
	python3 -m venv venv; source venv/bin/activate.fish; pip3 install -r requirements.txt; deactivate

.PHONY: format
format:
	source venv/bin/activate; black . --exclude venv
