FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    gdal-bin \
    python3

RUN ln -s /usr/bin/python3 /usr/bin/python

WORKDIR /app
COPY . /app

CMD ["python", "script.py"]
