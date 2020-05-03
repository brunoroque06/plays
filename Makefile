.PHONY: prepare
prepare:
	make -C blockchain prepare
	make -C dijkstra prepare

.PHONY: test
test:
	make -C blockchain test
	make -C dijkstra test
	make -C geneticalgorithm test
	make -C oop-limitations test
