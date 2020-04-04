#!/bin/bash
source ../venv/bin/activate
export FLASK_ENV=testing
DIR=$(pwd)
BOLD=$(tput bold)
NORMAL=$(tput sgr0)
GREEN='\033[0;32m'

while true; do
    case "$1" in
        -c | --coverage ) \
            coverage run --source=./ -m unittest discover -s tests/ --verbose \
            && coverage html \
            && printf "\n${BOLD}---> ${GREEN}Coverage results in ${NORMAL}${DIR}/htmlcov/index.html\n\n"; \
            break;;
        * ) python -m unittest discover -s tests/ --verbose; break;;
    esac
done