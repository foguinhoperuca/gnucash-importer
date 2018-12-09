FROM ubuntu:rolling
MAINTAINER Jefferson Campos <jefferson@jeffersoncampos.eti.br>

ENV DEBIAN_FRONTEND noninteractive 

# source: https://gist.github.com/dergachev/8441335
# FIXME hard-coded IP from quid-deb-proxy server
RUN echo "Acquire::http::Proxy \"http://192.168.1.101:8000\";" > /etc/apt/apt.conf.d/30proxy
RUN	echo "Acquire::http::Proxy::ppa.launchpad.net DIRECT;" >> /etc/apt/apt.conf.d/30proxy
RUN cat /etc/apt/apt.conf.d/30proxy

# RUN apt-get install squid-deb-proxy-client # FIXME really need it?
RUN apt-get update && apt-get install -y --no-install-recommends \
  gnucash \
  python3-gnucash \
  python3 \
  python3-dev \
  python3-pip \
  build-essential \
  python3-setuptools \
  zlib1g-dev \
  git \
  vim \
  dconf-cli \
  dbus-x11 \
  vanilla-gnome-desktop \
&& rm -rf /var/lib/apt/lists/*

RUN pip3 install -U pip setuptools

WORKDIR /app
COPY . /app

RUN pip3 install -r requirements.txt
