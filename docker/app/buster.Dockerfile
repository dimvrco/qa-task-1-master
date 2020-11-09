FROM osgeo/gdal:ubuntu-small-3.2.0
# FROM python:3.8-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

RUN apt-get update && \
	apt-get install --no-install-recommends -y \
		gcc \
		g++ \
		python3 \
		python3-dev \
		python3-pip \
		xz-utils \
		&& \
	apt-get clean && \
	apt-get autoremove && \
	rm -rf /var/lib/apt/lists/*

ADD ./app /app
RUN pip3 install --no-cache-dir -r /app/requirements.txt

ADD ./docker/app/docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod 755 /docker-entrypoint.sh
WORKDIR /app/

ENTRYPOINT ["/docker-entrypoint.sh"]
