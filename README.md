# GNUCash Parser

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
