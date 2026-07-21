# -*- mode: python ; coding: utf-8 -*-
# Onedir build so the installer can ship a full application folder.

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('assets', 'assets'),
        ('plugins', 'plugins'),
        ('core_debug_tools', 'core_debug_tools'),
        ('LICENSE.md', '.'),
        ('LICENSE', '.'),
        ('README.md', '.'),
        ('VERSION.txt', '.'),
        ('requirements.txt', '.'),
        ('assets/koromali.ico', '.'),
    ],
    hiddenimports=['PyQt6.sip', 'jedi', 'qtawesome.icon_browser'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Koromali',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='assets/koromali.ico',
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Koromali',
)
