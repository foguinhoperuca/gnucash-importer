# GNUCash Importer

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

