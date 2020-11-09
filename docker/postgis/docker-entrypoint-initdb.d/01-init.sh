#!/bin/bash
# set -xe

# substitute environment variables into init scripts
SCRIPTS_DIR=/docker-entrypoint-initdb.d
SELF_FILE=$(basename $0)
TMP_DIR=/tmp/moo
mkdir -p $TMP_DIR
for SCRIPT_PATH in $SCRIPTS_DIR/*; do
	SCRIPT_FILE=$(basename $SCRIPT_PATH)
	if [ "$SELF_FILE" == "$SCRIPT_FILE" ]; then
		echo "Skipping envsubst on self"
	else
		echo "Substituting env vars in $SCRIPT_PATH"
		envsubst < $SCRIPT_PATH > $TMP_DIR/$SCRIPT_FILE
		# scripts that require vars after envsubst should use '$'VARNAME instead of $VARNAME. The next line then cleans them up
		sed -i s/\'$\'/$/g $TMP_DIR/$SCRIPT_FILE
		mv $SCRIPTS_DIR/$SCRIPT_FILE $SCRIPTS_DIR/$SCRIPT_FILE.old
		mv $TMP_DIR/$SCRIPT_FILE $SCRIPTS_DIR/$SCRIPT_FILE
	fi
done
rmdir $TMP_DIR
