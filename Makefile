.PHONY: prepare
prepare:
	(cd blockchain/; make prepare)
	(cd data-analytics/; make prepare)
	(cd geneticalgorithm/; make prepare)

.PHONY: test
test:
	(cd blockchain/; make test)
	(cd decision-tree-player/; make test)
	(cd geneticalgorithm/; make test)
