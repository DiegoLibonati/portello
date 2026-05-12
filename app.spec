# -*- mode: python ; coding: utf-8 -*-
#
# IMPORTANT — Production .env handling
# ------------------------------------
# The `.env` file bundled below MUST be a dedicated production env file
# (for example `dist.env` or `.env.prod`), NOT the development `.env`
# you use locally to point at the dev Docker MongoDB.
#
# The recommended workflow is to create a separate `.env.prod` (or
# `dist.env`) containing real production credentials, copy it to `.env`
# only at build time (or change the path below), and ensure it never
# gets committed to source control. Never place real secrets in the
# repo-level `.env`.

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

