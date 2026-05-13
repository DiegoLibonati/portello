# -*- mode: python ; coding: utf-8 -*-
#
# IMPORTANT — Production .env handling
# ------------------------------------
# Before running PyInstaller, set production credentials directly in `.env`.
# `.env` is gitignored and will not be committed. Do not reuse the
# development `.env` that points at the dev Docker MongoDB; replace its
# values with real production credentials at build time.

a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=[],
    datas=[('.env', '.')],  # See note above: this should be the prod env file.
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure, a.zipped_data)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
    onefile=True,
)

