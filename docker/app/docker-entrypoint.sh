#! /usr/bin/env bash
set -e

PATH_PY_REQS='/app/requirements.txt'
DIR_PKG_JSON='/app/static'

if [ -f $PATH_PY_REQS ]; then
	echo "installing '$PATH_PY_REQS'..."
	pip3 install --upgrade pip --no-cache-dir -r $PATH_PY_REQS
fi

PATH_PKG_JSON="$DIR_PKG_JSON/package.json"
if [ -f $PATH_PKG_JSON ]; then
	echo "installing '$PATH_PKG_JSON'..."
	npm install --prefix $DIR_PKG_JSON
fi

exec "$@"