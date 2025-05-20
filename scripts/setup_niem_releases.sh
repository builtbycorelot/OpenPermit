#!/bin/sh
# Initialize the NIEM-Releases submodule at tag 6.0
# Usage: bash scripts/setup_niem_releases.sh
set -e

REPO_PATH="openpermit/standards/niem/NIEM-Releases"

if [ -d "$REPO_PATH" ]; then
    echo "NIEM-Releases already exists at $REPO_PATH"
    exit 0
fi

# Add the submodule
git submodule add https://github.com/NIEM/NIEM-Releases "$REPO_PATH"
cd "$REPO_PATH"
# Checkout the 6.0 tag
git checkout tags/6.0
cd - >/dev/null

echo "NIEM-Releases cloned to $REPO_PATH at tag 6.0"
