#!/usr/bin/env python3
from lilaclib import *
import os

update_on = [{'aur': None}]
build_prefix = 'extra-x86_64'
depends = ['wiredtiger']
build_args = ['-r', os.path.expanduser('~/.lilac/archbuild')]
time_limit_hours = 4
pre_build = aur_pre_build
post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
