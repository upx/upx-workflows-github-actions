#! /usr/bin/env python3
## vim:set ts=4 sw=4 et: -*- mode: python; coding: utf-8 -*-
## Copyright (C) Markus Franz Xaver Johannes Oberhumer

from string import Template
class MyTemplate(Template):
    delimiter = '§'

vars = {
    'runs_on': 'ubuntu-latest',
}

yaml = MyTemplate(r'''
# Copyright (C) Markus Franz Xaver Johannes Oberhumer
# see https://github.com/crate-ci/typos

name: 'Misc - Spell check 2'
"on":
# schedule: [cron: '55 0 * * 3'] # run weekly Wednesday 00:55 UTC
  workflow_dispatch: null
env:
  DEBIAN_FRONTEND: noninteractive

  # these are exactly like the GITHUB_xxx default environment variables
  REMOTE_REF_NAME: devel
  REMOTE_REF_TYPE: branch         # branch OR tag
  REMOTE_REPOSITORY: upx/upx
  REMOTE_SERVER_URL: https://github.com
  REMOTE_SHA: "0000000000000000000000000000000000000000" # will get updated below

jobs:
  job-spell-check:
    if: github.repository_owner == 'upx'
    name: 'Spell check'
    runs-on: §{runs_on}
    steps:

      - name: 'Display environment'
        run: |
          uname -a; pwd; id; umask
          env -0 | LC_ALL=C sort -z | tr '\000' '\n'

      - name: ${{ format('Check out {0}/{1} {2} {3} source code', env.REMOTE_SERVER_URL, env.REMOTE_REPOSITORY, env.REMOTE_REF_TYPE, env.REMOTE_REF_NAME) }}
        run: |
          # git config
          git config --global core.autocrlf false
          git config --global --add safe.directory '*'
          # install Self, needed for config file below
          git clone --branch "$GITHUB_REF_NAME" --depth 1 "$GITHUB_SERVER_URL/$GITHUB_REPOSITORY" ../Self

          git clone --branch "$REMOTE_REF_NAME" --depth 1 "$REMOTE_SERVER_URL/$REMOTE_REPOSITORY" .
          test -f ./.gitmodules && git submodule update --init
          # TODO: handle REMOTE_REF_TYPE == "tag"
          # update environment
          rev="$(git rev-parse HEAD)"
          echo "REMOTE_SHA=$rev" >> $GITHUB_ENV

      - name: 'Spell check with crate-ci/typos'
        uses: crate-ci/typos@5bd389de715c63ba86568420809e324fcea78660 # v1.16.25
        with: { config: ../Self/.github/typos_config_upx.toml }
''')

print(yaml.substitute(vars).strip())
