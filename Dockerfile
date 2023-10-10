FROM python:latest

RUN apt-get update && apt-get install -y \
  wget \
  software-properties-common \
  ca-certificates \
  curl \
  gnupg \
  gcc \
  bsdmainutils \
  make

WORKDIR /app

COPY . .

RUN make install
