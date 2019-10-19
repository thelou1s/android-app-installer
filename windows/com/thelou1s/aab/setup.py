#! /usr/bin/env python
# -*- coding: utf-8 -*-
# https://cx-freeze.readthedocs.io/en/latest/distutils.html#distutils-setup-script

from cx_Freeze import setup, Executable

base = None
# base = 'Console'
# base = 'ConsoleKeepPath'
# base = 'Win32GUI'
# base = 'Win32Service'

executables = [
    Executable('Test6.py', base = base)
]

build_exe_options = {"includes": ["res"]}


setup(name = 'App',
      version = 'v1.0',
      description = 'main app',
      executables = executables,
      options = {'build_exe': build_exe_options}
      )