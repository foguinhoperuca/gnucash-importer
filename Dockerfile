FROM ubuntu:latest
MAINTAINER Jefferson Campos <jefferson@jeffersoncampos.eti.br>

ENV DEBIAN_FRONTEND noninteractive 
RUN apt-get update && apt-get install -y \
  gnucash \
  dbus-x11 \
  libdbi1 \
  libdbd-sqlite3 \
  libdbd-pgsql \
  libdbd-mysql \
  python3 \
  pip3\
  python3-gnucash \
&& rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["/usr/bin/gnucash", "--logto", "stderr"]
