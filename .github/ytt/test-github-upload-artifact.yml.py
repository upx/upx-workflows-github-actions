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
      - name: 'Upload artifact job-§{nice_name}'
        uses: actions/upload-artifact@v4
        with:
          name: 'job-§{nice_name}'
          path: test.txt
''')

containers = [
    # Alma Linux (RHEL)
    'almalinux:8',
    'almalinux:9',
    # Alpine Linux
    'alpine:3.1', 'i386/alpine:3.1',
    'alpine:3.8', 'i386/alpine:3.8',
    'alpine:3.9', 'i386/alpine:3.9',
    'alpine:3.10', 'i386/alpine:3.10',
    'alpine:3.11', 'i386/alpine:3.11',
    'alpine:3.19', 'i386/alpine:3.19',
    'alpine:3.20', 'i386/alpine:3.20',
    'alpine:3.21', 'i386/alpine:3.21',
    'alpine:3.22', 'i386/alpine:3.22',
    'alpine:edge', 'i386/alpine:edge', # rolling
    # Arch Linux
    'archlinux:latest', # rolling
    # CentOS (RHEL)
    'quay.io/centos/centos:centos7', # EOL 2024-06-30
    'quay.io/centos/centos:stream8', # EOL 2024-05-31
    'quay.io/centos/centos:stream9',
    'quay.io/centos/centos:stream9-minimal',
    # Chimera Linux
    'chimeralinux/chimera:latest', # rolling
    # Debian Linux
    'debian:10-slim', 'i386/debian:10-slim',
    'debian:11-slim', 'i386/debian:11-slim',
    'debian:12-slim', 'i386/debian:12-slim',
    'debian:testing-slim',  'i386/debian:testing-slim',  # rolling
    'debian:unstable-slim', 'i386/debian:unstable-slim', # rolling
    # Fedora Linux
    'fedora:30',
    'fedora:42',
    'fedora:rawhide', # rolling
    # openSUSE
    'opensuse/leap:15.0',
    'opensuse/leap:15.1',
    'opensuse/leap:15.2',
    'opensuse/leap:15.3',
    'opensuse/leap:15.4',
    'opensuse/leap:15.5',
    'opensuse/leap:15.6',
    'opensuse/leap:latest',
    'opensuse/tumbleweed:latest', # rolling
    # Rocky Linux (RHEL)
    'rockylinux:8',
    'rockylinux:9',
    # UBI RedHat (RHEL)
    'registry.access.redhat.com/ubi7/ubi-minimal',
    'registry.access.redhat.com/ubi8/ubi-micro',
    'registry.access.redhat.com/ubi8/ubi-minimal',
    'registry.access.redhat.com/ubi9/ubi-micro',
    'registry.access.redhat.com/ubi9/ubi-minimal',
    # Ubuntu Linux
    'ubuntu:12.04',
    'ubuntu:14.04',
    'ubuntu:16.04',
    'ubuntu:18.04',
    'ubuntu:20.04',
    'ubuntu:22.04',
    'ubuntu:24.04',
    # Void Linux
    'ghcr.io/void-linux/void-glibc', # rolling
    'ghcr.io/void-linux/void-musl',  # rolling
]

jobs = ''
for container in containers:
    nice_name = container
    nice_name = re.sub(r'^ghcr\.io/', '', nice_name)
    nice_name = re.sub(r'^quay\.io/centos/', '', nice_name)
    nice_name = re.sub(r'^registry\.access\.redhat\.com/', '', nice_name)
    nice_name = re.sub(r'[^0-9a-zA-Z-]', '_', nice_name)
    vars = {
        'container': container,
        'nice_name': nice_name,
    }
    jobs += '  ' + job_template.substitute(vars).strip() + '\n'

vars = { 'jobs': jobs }
print(main_template.substitute(vars).strip())
