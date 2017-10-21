# -*- mode: python -*-
import os

block_cipher = None

# path = os.path.dirname(os.path.realpath(%CD%))
# print(path)

a = Analysis(['../main.py'],
             pathex=['E:\\Works\\Git\\Tools\\BatchBuildLightUE4'],
             # pathex=[path],
             binaries=[],
             datas=[('../BatchLightUE4/Resources/*.png', 'BatchLightUE4/Resources')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='Batch Light UE4',
          debug=False,
          strip=False,
          upx=True,
          console=False ,
          # uac_admin=True,
          icon='E:\\Works\\Git\\Tools\\BatchBuildLightUE4\\Resources\\light-bulb-icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='Build Light')
