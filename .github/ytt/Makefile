YTT = ytt-0.46.0

.PHONY: PHONY
.SECONDEXPANSION:
.SUFFIXES:

BUILT_FILES :=
BUILT_FILES += ../workflows/misc-spell-check.yml

default: PHONY $(BUILT_FILES)

../workflows/%.yml : %.yml $(MAKEFILE_LIST)
	@echo '# Copyright (C) Markus Franz Xaver Johannes Oberhumer' > $@
	$(YTT) -f- < $< >> $@

.DELETE_ON_ERROR: $(BUILT_FILES)
