# /app_core/config.py

# This file contains static, foundational configuration constants
# and should have NO local application imports to prevent circular dependencies.

import os

APP_NAME = "Koromali"
ORG_NAME = os.environ.get("KOROMALI_ORG_NAME", "Koromali")

# GitHub related metadata is configurable so that the repository can be
# distributed without including identifying information for the maintainer's
# login.  Downstream users may override these values via environment variables.
GITHUB_REPO_URL = os.environ.get("KOROMALI_GITHUB_REPO_URL", "")
GITHUB_ISSUES_URL = os.environ.get("KOROMALI_GITHUB_ISSUES_URL", "")
GITHUB_PLUGINS_REPO = os.environ.get("KOROMALI_GITHUB_PLUGINS_REPO", "")