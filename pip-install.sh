#!/usr/bin/env bash

if [ "$1" == "" ]; then
    printf "Package name required. exiting ..\n"
    exit
fi

pip install $1 && pip freeze | grep $1 >> requirements.txt
