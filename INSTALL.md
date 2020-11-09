# Example admin console

This is a sample admin console project.

##### Requirements

- Docker (tested on v19.03.12)
- [docker-compose](https://github.com/docker/compose/releases) (may need to be installed separately depending on your OS)

## Getting started

Build the images, start the dev environment, and get a shell inside the app container:

```bash
docker-compose build
docker-compose up -d
docker exec -it ca-app bash
```

Initialize the django app and start the dev server:

```bash
# inside the app container
cd /app
python3 manage.py migrate
python3 manage.py createsuperuser
# enter arbitrary creds for the first admin user
python3 manage.py runserver 0.0.0.0:80
```

Assuming you did not change the port mapping in the docker-compose file, the app console should be available at [http://localhost:8080](http://localhost:8080). The pgadmin console (for viewing the dev database) is available at [http://localhost:8081](http://localhost:8081).

## Django testing

Django tests should be run with the `--keepdb` argument because the app DB is unmanaged and requires custom setup done as part of the postgis container setup.

```bash
python3 manage.py test --keepdb
```

## Nightwatch testing

Nightwatch tests can be run from the './nightwatch/' directory. Detailed instructions are provided in the 'README.md' in that directory. Test specs are contained in './nightwatch/test/specs/'. The condensed version of running nightwatch tests is:

```bash
cd ./nightwatch

# run once
docker-compose build
docker-compose up -d chromedriver

# execute tests
docker-compose up nightwatch
```
