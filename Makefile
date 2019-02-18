SUBDIRS := $(wildcard */.)

make_sub_dirs = $(foreach dir, $(SUBDIRS), $(call make_question,$(1),$(dir)); $(did_make_fail) && $(call make,$(1),$(dir)) || $(call print_error,$(dir)))
make_question = $$($(MAKE) $(1) --question --directory $(2)) 
did_make_fail = test $$(printf "$$?") -le 1
make = $(MAKE) $(1) --directory $(2)
print_error = printf "Folder's '%s' Makefile does not contain target.\n" $(1)

.PHONY: prepare
prepare:
	@$(call make_sub_dirs,prepare)

.PHONY: test
test:
	@$(call make_sub_dirs,test)
