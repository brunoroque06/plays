.PHONY: prepare
prepare: 
	(cd geneticalgorithm/; make prepare)

.PHONY: test
test: 
	(cd decision-tree-player/; make test)
	(cd geneticalgorithm/; make test)
