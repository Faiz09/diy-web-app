#!/usr/bin/env bash

if [ "$1" = '' ]; then
    exit
fi

python -m pytest -q -s -m live "$1"