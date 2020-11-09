FROM osgeo/gdal:alpine-small-3.1.2

# core packages
RUN apk add --no-cache bash \
	geos>3.7.0 \
	postgresql-client>12.0.0 \
	python3>3.7.0 \
	py3-pip

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app
# ENV NODE_VER=14.2.0

# RUN groupadd -r app && \
#     useradd --no-log-init -r -g app app -m

# uncomment below to add node
# ADD https://nodejs.org/dist/v$NODE_VER/node-v$NODE_VER-linux-x64.tar.xz /node.tar.xz
# RUN tar -xf node.tar.xz && \
#     cp node-v$NODE_VER-linux-x64/* /usr/ -rf

# RUN npm install -g less

# ADD --chown=app:app ./app/static/package*.json /app/static
# RUN npm install --prefix /app/static

ADD ./app/requirements.txt /app/requirements.txt
RUN apk add --no-cache --virtual .build-deps \
		gcc \
		gdal-dev==3.1.4-r0 \
		python3-dev \
		musl-dev \
		zlib-dev \
		libxml2-dev \
		build-base \
		postgresql-dev && \
	pip3 install --no-cache-dir -r /app/requirements.txt && \
	apk del .build-deps

ADD ./app /app
ADD ./docker/app/docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod 755 /docker-entrypoint.sh
WORKDIR /app/

ENTRYPOINT ["/docker-entrypoint.sh"]
