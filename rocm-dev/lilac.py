#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
update_on = [{'aur': None}]
repo_depends = [
        'comgr',
        'hip-rocclr',
        'hsa-amd-aqlprofile',
        'hsa-ext-rocr-bin',
        'hsa-rocr',
        'hsakmt-roct',
        'llvm-amdgpu',
        'rocm-cmake',
        'rocm-dbgapi',
        'rocm-debug-agent',
        'rocm-device-libs',
        'rocm-gdb',
        'rocm-smi',
        'rocm-smi-lib64',
        'rocm-utils',
        'rocprofiler',
        'roctracer',
        ]
build_prefix = 'extra-x86_64'
pre_build = aur_pre_build
post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
