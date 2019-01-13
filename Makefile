prepare: 
	(cd geneticalgorithm/; make prepare)

test: 
	(cd decision-tree-player/; make test)
	(cd geneticalgorithm/; make test)

.PHONY: prepare test
