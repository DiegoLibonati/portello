# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [v1.1.0] - 2026-05-16

### Features

- feat: .python-version file added (a3586ea)
- feat: added new test step in CI (7140a0f)
- feat: added ci lint - ruff - audit - build (715a88b)
- feat: remove loggers info (2bf62a7)
- feat: better readme (606275b)
- feat: added .dockerignore file (e264592)
- feat: better structure by tkinter template (6aef36e)
- feat: added build files (f3f1db2)
- feat: better exports, new build system and pre-commit added and better structure tkinter project (64faf67)
- feat: better code and tests added (a4472ab)

### Bug fixes

- fix: redirect egg-info to project root to prevent it from being generated inside src/ and user model pydantic fix (d4c7d1c)
- fix:The fix is in pyproject.toml:50-61. pytest-env sets env vars into the live process before any fixture runs, so the docker_db fixture's subprocess.run(['docker', 'compose', ...]) inherits them. Previously, MONGO_USER and MONGO_PASS were never set (only the TEST_MONGO_* aliases were), so docker-compose  initialized MongoDB with empty/blank credentials while the connection URI kept using admin:secret123. (8d11148)
- fix: ci prod and fix ruff lint files (0051a45)
- fix: fix vulnerabilities (1e22816)
- fix: better docker composes (b2cd2be)
- fix: better tests (c33c922)
- fix: title app (8bbaa2a)
- fix: use env keys from pyproject.toml in pytest options in tests (554978a)
- fix: better repository name/description and better system test (5c8c855)
- fix: remove migrations exclude in pre commit config and update requirements dev and remove deprecated pydantic v1 constr (27d1b0f)
- fix: fix build exe with nex config app.spec (beaae68)

### Refactors

- refactor: replace pip install -r with pip install -e for build, dev and test deps (58e581d)
- refactor: migrate deps to pyproject.toml and update README. (d05f1fc)
- refactor: test suite to align with project testing standards and structure standars (1075264)

### Documentation

- docs: simplify production env setup to use .env directly (23da974)

### Build & CI

- ci: trigger first release (79b3be4)
- ci: run lint-and-audit, test, and build sequentially (1f29136)

### Uncategorized

-  ci: add mypy gate and automated release pipeline (210aad4)
- patch: readme updated (96bce45)
- patch: readme updated (001a974)
- patch: readme updated (b83bcde)
- Update README.md (8d4f6eb)
- New structure of project with types (d0e5d4a)
- Update README.md (0a0c27b)
- fix link (6d9b681)
- readme fix (d5e689e)
- New readme (7fdaec6)
- Update README.md (defc0b3)
- New readme (5a9eaa9)
- New repository! (1a8d7b0)
- Initial commit (7ac7578)

