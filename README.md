# GNUCash Importer

[![Build Status](https://travis-ci.org/foguinhoperuca/gnucash_magical_importer.svg?branch=master)](https://travis-ci.org/foguinhoperuca/gnucash_magical_importer)

Set of scripts to manage my personal finance with gnucash. This project have many parsers to gnucash file. The intent is integrate diferents data sources into gnucash data file.

The gnucash's xml file will act as transaction database. All other reports will be born from Parsers.

## Source of Information

* Nubank credit card
* Itau's checking account
* CEF's savings
* Bradesco's savings
* Gnucash mobile (untracked expenses: money in wallet, gifts, etc)

# Requirements

* Cronjob to run integrations
* From any data source, all transactions must be integrate into one file
* one file with git commits
* Report of imported files
* Save gnucash's xml file as regular file instead of binary (compressed) - it can be achived with option file-compression=false in [general section of gnucash configuration](test/fixtures/gnucash.conf "Example configuration")

# Financial Management

## Source of transactions

* Itau Checking Account
* CEF savings
* Bradesco savings
* Money in wallet
* Nubank

# Classifier

# Main goal

* Single transaction

# More Complex Operations

* A transaction that's is part of another big transaction (a buy with stallments)
* Monthly (recurrent) payment: HAVAN, RCHLO and utilities bill (gas, water, eletricity)

# Similar Projects

* https://github.com/tdf/pygnclib
* https://github.com/hjacobs/gnucash-fiximports
* https://github.com/hjacobs/gnucash-qif-import
* https://krzysztofzuraw.com/blog/2016/makefiles-in-python-projects.html
* https://github.com/sdementen/gnucash-utilities
* https://github.com/wesabe/fixofx (has a fakeofx.py to genarete fixtures)
* https://gist.github.com/foguinhoperuca/ef11a07937e531b5d0e98271f1422de5 (css style for doc)

# Enviroment

It can't be used with virtualenv beacause of dependency on python3-gnucash deb package and gnucash itself.
So, you'll need install direct in OS with command:
```
jefferson@nami.jeffersoncampos.eti.br: ~/universal/projects/gnucash/gnucash-importer/ $ pip3 install -r requirements.txt
```

## Docker

For dev machine, you can use docker to development. Build docker with
```
jefferson@nami.jeffersoncampos.eti.br: ~/universal/projects/gnucash/gnucash-importer/ $ sudo docker build -t foguinhoperuca/gnucash_magical_importer . --build-arg USE_APT_PROXY=True --build-arg APT_PROXY=192.168.1.101:8000
```
or
```
jefferson@nami.jeffersoncampos.eti.br: ~/universal/projects/gnucash/gnucash-importer/ $ make docker_build
```

Then, run the tests with:

```
jefferson@nami.jeffersoncampos.eti.br: ~/universal/projects/gnucash/gnucash-importer/ $ docker run -ti foguinhoperuca/gnucash_magical_importer /bin/sh -c "make unittest"
```
or
```
jefferson@nami.jeffersoncampos.eti.br: ~/universal/projects/gnucash/gnucash-importer/ $ make docker_run
```

# Hacking with bdsit-wheel

0. manually create egg-info bdsit (bdist_egg) and copy it with expected name as gnucash_magical_importer-0.1.0-py3.6.egg-info in directory build/bdsit.linux-x86_64/wheel;
1. Comment lines in python3 source code: sudo vim /usr/lib/python3.6/email/message.py#558 and #559;
2. Then, run python3 setup.py sdist bdist_wheel;
3. finally, revert step 2;

https://github.com/pypa/wheel/blob/master/wheel/bdist_wheel.py
