PYTHON3 = python3
YQ      = yq
YTT     = ytt

.PHONY: PHONY
.SECONDEXPANSION:
.SUFFIXES:

BUILT_FILES :=
BUILT_FILES += ../workflows/cc-container-alpine-clang.yml
BUILT_FILES += ../workflows/cc-container-alpine-cross-mingw32-gcc-i386.yml
BUILT_FILES += ../workflows/cc-container-alpine-cross-mingw32-gcc.yml
BUILT_FILES += ../workflows/cc-container-alpine-cross-mingw64-gcc.yml
BUILT_FILES += ../workflows/cc-container-alpine-gcc.yml
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

define verify-yaml
	@$(YTT) -f- < $1 > /dev/null
	@$(YQ) < $1 > /dev/null
endef

DEPS = $(MAKEFILE_LIST) | ../workflows/.

../workflows/%.yml : %.yml $(DEPS)
	$(call verify-yaml,$<)
	$(call header,$@)
	$(YTT) -f- < $< | $(YQ) >> $@
	$(call verify-yaml,$@)

../workflows/%.yml : %.yml.py $(DEPS)
	$(call header,$@)
	$(PYTHON3) $< | $(YTT) -f- | $(YQ) >> $@
	$(call verify-yaml,$@)

# directories
%/. : ; @mkdir -p -v "$(patsubst %/,%,$(dir $@))"
.PRECIOUS: %/.

clean: PHONY
	rm -f $(BUILT_FILES)

.DELETE_ON_ERROR: $(BUILT_FILES)
