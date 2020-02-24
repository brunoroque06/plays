.PHONY: prepare
prepare:
	make -C blockchain prepare
	make -C geneticalgorithm prepare

.PHONY: test
test:
	make -C blockchain test
	make -C geneticalgorithm test
