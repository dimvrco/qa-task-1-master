#!/bin/bash
set -xe
# for migrations in both app and test_app

for FILE in /docker-entrypoint-initdb.d/*.manual; do
	echo '$'FILE
	PGPASSWORD=$POSTGRES_PASSWORD psql -U $POSTGRES_USER -d $POSTGRES_DB -f '$'FILE

	# test db must match /app/core_admin/settings/DATABASES.app
	PGPASSWORD=$POSTGRES_PASSWORD psql -U $POSTGRES_USER -d $TEST_POSTGRES_DB -f '$'FILE
done
