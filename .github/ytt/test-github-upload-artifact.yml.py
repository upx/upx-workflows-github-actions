#! /usr/bin/env python3
## vim:set ts=4 sw=4 et: -*- mode: python; coding: utf-8 -*-
## Copyright (C) Markus Franz Xaver Johannes Oberhumer

import re
from string import Template
class MyTemplate(Template):
    delimiter = '§'

main_template = MyTemplate(r'''
# Copyright (C) Markus Franz Xaver Johannes Oberhumer
# see https://github.com/actions/upload-artifact

# test upload-artifact from various containers

name: 'Test GitHub @actions/upload-artifact'
'on':
  workflow_dispatch: null
env:
  DEBIAN_FRONTEND: noninteractive

jobs:
§{jobs}
''')

job_template = MyTemplate(r'''
  'job-§{nice_name}':
    container: '§{container}'
    runs-on: ubuntu-latest
    steps:
      - name: 'Make artifact'
        run: 'echo TEST > test.txt'
      - name: 'Upload artifact §{nice_name}'
        uses: actions/upload-artifact@v4
        with:
          name: 'job-§{nice_name}'
          path: test.txt
''')

containers = [
    'alpine:3.1', 'i386/alpine:3.1',
    'alpine:3.8', 'i386/alpine:3.8',
    'alpine:3.9', 'i386/alpine:3.9',
    'alpine:3.19', 'i386/alpine:3.19',
    'alpine:edge', 'i386/alpine:edge',
    'chimeralinux/chimera:latest',
    'debian:10-slim', 'i386/debian:10-slim',
    'debian:11-slim', 'i386/debian:11-slim',
    'debian:12-slim', 'i386/debian:12-slim',
    'opensuse/leap:latest',
    'opensuse/tumbleweed:latest',
    'redhat/ubi8-minimal:latest',
    'redhat/ubi8-micro:latest',
    'redhat/ubi9-minimal:latest',
    'redhat/ubi9-micro:latest',
    'ubuntu:12.04',
    'ubuntu:18.04',
    'ubuntu:20.04',
]

jobs = ''
for container in containers:
    vars = {
        'container': container,
        'nice_name': re.sub(r'[^0-9a-zA-Z-]', '_', container),
    }
    jobs += '  ' + job_template.substitute(vars).strip() + '\n'

vars = { 'jobs': jobs }
print(main_template.substitute(vars).strip())
