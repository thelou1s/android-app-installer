# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['/Users/luis/PycharmProjects/PySimpleGUITest/venv/src/app.aab'],
             pathex=['/Users/luis/PycharmProjects/PySimpleGUITest/venv/src'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='app',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='/Users/luis/PycharmProjects/PySimpleGUITest/venv/src/bundletool-all-0.10.2.jar')
app = BUNDLE(exe,
             name='app.app',
             icon='/Users/luis/PycharmProjects/PySimpleGUITest/venv/src/bundletool-all-0.10.2.jar',
             bundle_identifier=None)
