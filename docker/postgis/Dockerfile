FROM postgres:12

RUN echo 'deb http://apt.postgresql.org/pub/repos/apt/ buster-pgdg main' > /etc/apt/sources.list.d/pgdg.list

RUN apt update -qy && \
	apt install -qy curl ca-certificates gnupg gettext-base && \
	curl https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - && \
	apt install -qy postgresql-12-postgis-3 && \
	rm -rf /var/lib/apt/lists/*

COPY ./postgis/docker-entrypoint-initdb.d/* /docker-entrypoint-initdb.d/
RUN ["chown", "postgres:postgres", "/docker-entrypoint-initdb.d", "-R"]
