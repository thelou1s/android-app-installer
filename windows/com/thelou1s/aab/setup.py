#! /usr/bin/env python
# -*- coding: utf-8 -*-
# https://cx-freeze.readthedocs.io/en/latest/distutils.html#distutils-setup-script

from cx_Freeze import setup, Executable
from sys import platform

base = None
if platform == "win32":
    base = "Win32GUI"
# base = 'Console'
# base = 'ConsoleKeepPath'
# base = 'Win32GUI'
# base = 'Win32Service'

executables = [
    Executable('Test6.py', base=base)
]

includefiles = ['res/adb', 'res/bundletool-all-0.10.2.jar', 'res/imoblife.android.keystore']
includes = []
excludes = ['Tkinter']
packages = ['do', 'khh']

build_exe_options = {"includes": ["res"]}
# https://stackoverflow.com/questions/2553886/how-can-i-bundle-other-files-when-using-cx-freeze



setup(name='App',
      version='1.0',
      description='main app',
      executables=executables,
      author='thelou1s',
      author_email='thelou1s@yahoo.com',
      options={'build_exe': {'includes': includes, 'excludes': excludes, 'include_files': includefiles}},
      )
