.PHONY: prepare
prepare: 
	virtualenv venv; source venv/bin/activate; pip3 install -r requirements.txt; deactivate

.PHONY: run
run: 
	source venv/bin/activate; jupyter lab PokemonWalls.ipynb
