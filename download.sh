#!/bin/sh
# the script may be executed from a symlink
script_home=$(dirname $(realpath "$0"))
. "$script_home"/venv/bin/activate

python3 "$script_home"/download.py $@

