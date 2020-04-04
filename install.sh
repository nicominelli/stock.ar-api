#!/usr/bin/env bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
cd "$DIR"
printf "===> Trying to install requirements for the project.\n\n"
virtualenv --python=python3.7 ../venv \
 && source ../venv/bin/activate \
 && pip install -r requirements.txt
printf "\n===> Installation complete.\n\n"
printf "Type './run.sh' for running the project.\n"