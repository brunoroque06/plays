.PHONY: prepare
prepare:
	make -C blockchain prepare

.PHONY: test
test:
	make -C blockchain test
	make -C decision-tree-player test
