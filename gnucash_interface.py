#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Meant to be reuseable interface with gnucash

'''

import datetime
from gnucash import Session, Transaction, Split, GncNumeric

def create_gnucash_tansaction(book, item, curr):
    print "TODO stub: Creating a GNUCash transaction"
    # TODO get correct accounts
    acc_from = ""
    acc_to = ""
    amount = 0                  # TODO calc amount

    if curr is None:
        curr = "BRL"

    if item is None:
        item = ""               # TODO throw an exception

    if book is None:
        book = ""               # TODO throw an exception

    tx = Transaction(book)
    tx.BeginEdit()
    tx.SetCurrency(curr)
    tx.SetDateEnteredTS(datetime.datetime.now())
    tx.SetDatePostedTS(item.date)
    tx.SetDescription(item.memo)

    split_from = Split(book)
    split_from.SetParent(tx)
    split_from.SetAccount(acc_from)
    split_from.SetValue(0)      # TODO set correct value
    split_from.SetAmount(0)     # TODO set correct amount

    split_to = Split(book)
    split_to.SetParent(tx)
    split_to.SetAccount(acc_to)
    split_to.SetValue(0)        # TODO set correct value
    split_to.SetAmount(0)       # TODO set correct amount

    tx.CommitEdit()
    
def write_to_gnucash_file():
    print "TODO stub: Writing to GNUCash file"
