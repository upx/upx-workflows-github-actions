#! /usr/bin/env bash
## vim:set ts=4 sw=4 et:
## Copyright (C) Markus Franz Xaver Johannes Oberhumer
set -e; set -o pipefail

# cron weekday
perl -i -pe $'s,(cron: \'.*) (\d)\'\],$1 2\'\],;' *.yml
#                                        ^-- HERE is the new weekday

# repository
perl -i -pe 's,\b(REMOTE_REPOSITORY:)\s+([\w/-]+)$,$1 upx/upx-workflows-github-weekly,;' *.yml
# branch name
perl -i -pe 's,\b(REMOTE_REF_NAME:)\s+([\w/-]+)$,$1 devel,;' *.yml

#perl -i -pe 's,\b(REMOTE_REPOSITORY:)\s+([\w/-]+)$,$1 upx/upx-test-threads,;' *.yml
#perl -i -pe 's,\b(REMOTE_REF_NAME:)\s+([\w/-]+)$,$1 test-threads,;' *.yml
