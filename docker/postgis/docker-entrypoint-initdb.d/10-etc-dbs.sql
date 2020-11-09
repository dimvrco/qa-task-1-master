-- admin db
CREATE USER $ADMIN_POSTGRES_USER WITH ENCRYPTED PASSWORD '$ADMIN_POSTGRES_PASS';

CREATE DATABASE $ADMIN_POSTGRES_DB
	WITH 
	OWNER = $ADMIN_POSTGRES_USER
	ENCODING = 'UTF8'
	LC_COLLATE = 'en_US.utf8'
	CONNECTION LIMIT = -1;

GRANT ALL ON DATABASE $ADMIN_POSTGRES_DB TO $ADMIN_POSTGRES_USER;

-- test app db
CREATE DATABASE $TEST_POSTGRES_DB
	WITH 
	OWNER = $POSTGRES_USER
	ENCODING = 'UTF8'
	LC_COLLATE = 'en_US.utf8'
	CONNECTION LIMIT = -1;
