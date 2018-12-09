FROM ubuntu:rolling
MAINTAINER Jefferson Campos <jefferson@jeffersoncampos.eti.br>

ENV DEBIAN_FRONTEND noninteractive 

# # source: https://gist.github.com/dergachev/8441335
# # FIXME hard-coded IP - maybe use build script?!?! - Maybe echo "Acquire::http::proxy DIRECT;" >> /etc/apt/apt.conf.d/30proxy
# RUN echo "Acquire::http::Proxy \"http://192.168.1.101:8000\";" > /etc/apt/apt.conf.d/30proxy
# RUN echo "Acquire::http::Proxy::ppa.launchpad.net DIRECT;" >> /etc/apt/apt.conf.d/30proxy
# # RUN if [ "x$arg" = "x" ] ; then (echo "Acquire::http::Proxy \"http://192.168.1.101:8000\";" > /etc/apt/apt.conf.d/30proxy; echo "Acquire::http::Proxy::ppa.launchpad.net DIRECT;" >> /etc/apt/apt.conf.d/30proxy) ; else echo Argument is $arg ; fi
# RUN cat /etc/apt/apt.conf.d/30proxy

# # FIXME how to know the machine is from dev?
# # ENV DOCKER_APT_PROXY $(uname -a | awk '/Linux / {print $2}')
# ENV DOCKER_APT_PROXY True
# RUN echo $DOCKER_APT_PROXY
# RUN if [ $DOCKER_APT_PROXY = "True" ] ; then \
# 		echo "Acquire::http::Proxy \"http://192.168.1.101:8000\";" > /etc/apt/apt.conf.d/30proxy;\
# 		echo "Acquire::http::Proxy::ppa.launchpad.net DIRECT;" >> /etc/apt/apt.conf.d/30proxy;\
# 	else \
# 		echo "Not dev machine..." ;\
# 	fi

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

WORKDIR /app
COPY . /app
