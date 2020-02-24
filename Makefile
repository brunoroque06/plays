.PHONY: prepare
prepare:
	make -C blockchain prepare

.PHONY: test
test:
	make -C blockchain test
	make -C geneticalgorithm test
