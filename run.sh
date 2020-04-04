#!/usr/bin/env bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
cd "$DIR"
VENV_DIR=../venv
if [ ! -d "$VENV_DIR" ]; then
    /bin/bash ./install.sh
    echo
fi
printf "===> Attempting to run stock.ar\n\n"
source ../venv/bin/activate
export FLASK_ENV=development
export FLASK_APP=run.py
flask run