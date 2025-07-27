#!/usr/bin/env bash
set -e

if [ ! -d "venv" ]; then
    echo "[INFO] Erstelle virtuelle Umgebung..."
    python3 -m venv venv
fi
# shellcheck disable=SC1091
source venv/bin/activate
python -m pip install --quiet -r requirements.txt
python -m organizertool gui
