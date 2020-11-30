#!/usr/bin/env bash

# full_path=$(realpath $0)
dir_path=$(dirname $(realpath $0))
env_path=$(dirname $dir_path)/env/bin/activate

#echo "dir path:" $dir_path

echo activating Python virtual env
source $env_path

# start server
python $dir_path/manage.py runserver

echo deactivating Python virual env
deactivate