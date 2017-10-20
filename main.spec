# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['e:\\WORKS\\Git\\BatchBuildLightUE4'],
             binaries=[],
             datas=[('BatchLightUE4/Resources/*.png', 'BatchLightUE4/Resources')],
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
          name='Build Light',
          debug=False,
          strip=False,
          upx=True,
          console=False,
          uac_admin=True,
          icon='e:\\WORKS\\Git\\BatchBuildLightUE4\\BatchLightUE4\\Resources\\light-bulb.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='Batch Light UE4')

coll = COLLECT(exe,
                coll)
