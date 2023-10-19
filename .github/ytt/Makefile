PYTHON3 = python3
YTT     = ytt

.PHONY: PHONY
.SECONDEXPANSION:
.SUFFIXES:

BUILT_FILES :=
BUILT_FILES += ../workflows/cc-github-all-macos-11.yml
BUILT_FILES += ../workflows/cc-github-all-macos-12.yml
BUILT_FILES += ../workflows/cc-github-all-macos-13.yml
BUILT_FILES += ../workflows/cc-github-all-ubuntu-20.04.yml
BUILT_FILES += ../workflows/cc-github-all-ubuntu-22.04.yml
BUILT_FILES += ../workflows/misc-reuse-compliance-check.yml
BUILT_FILES += ../workflows/misc-spell-check.yml
BUILT_FILES += ../workflows/misc-spell-check2.yml

default: PHONY $(BUILT_FILES)

define header
	@echo '# Copyright (C) Markus Franz Xaver Johannes Oberhumer' > $1
	@echo '# DO NOT EDIT, GENERATED AUTOMATICALLY' >> $1
endef

DEPS = $(MAKEFILE_LIST) | ../workflows/.

../workflows/%.yml : %.yml $(DEPS)
	$(call header,$@)
	$(YTT) -f- < $< >> $@

../workflows/%.yml : %.yml.py $(DEPS)
	$(call header,$@)
	$(PYTHON3) $< | $(YTT) -f- >> $@

# directories
%/. : ; @mkdir -v $(dir $@)
.PRECIOUS: %/.

clean: PHONY
	rm -f $(BUILT_FILES)

.DELETE_ON_ERROR: $(BUILT_FILES)
