FROM ubuntu:rolling
MAINTAINER Jefferson Campos <jefferson@jeffersoncampos.eti.br>

ENV DEBIAN_FRONTEND noninteractive 

ARG USE_APT_PROXY=False
ARG APT_PROXY=192.168.1.101:8000
RUN if [ "$USE_APT_PROXY" = "True" ] ; then \
		echo "Acquire::http::Proxy \"http://$APT_PROXY\";" > /etc/apt/apt.conf.d/30proxy; \
		echo "Acquire::http::Proxy::ppa.launchpad.net DIRECT;" >> /etc/apt/apt.conf.d/30proxy; \
		echo "------------------- Beware, USING apt proxy!! -------------------"; \
	else \
		echo "------------------- NOT a DEV machine!! -------------------"; \
	fi

# TODO split this in various command to make more easy the installation
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

COPY requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt

COPY test/fixtures/gnucash.conf /tmp/
RUN dbus-launch dconf load /org/gnucash/ < /tmp/gnucash.conf

COPY setup.cfg /etc/gnucash-magical-importer/

WORKDIR /app
COPY . /app
