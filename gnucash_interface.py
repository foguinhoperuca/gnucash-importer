#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Meant to be reuseable interface with gnucash
'''

import datetime
from Decimal import decimal
from gnucash import Session, Transaction, Split, GncNumeric

def get_currency(book, curr = default_currency):
    commod_tab = book.get_table()
    currency = commod_tab.lookup('ISO4217', curr)

def create_gnucash_tansaction(book, item, curr):
    print "TODO stub: Creating a GNUCash transaction"
    # TODO get correct accounts
    acc_from = ""
    acc_to = ""
    amount = int(Decimal(item.split_amount.replace(',', '.')) * curr.get_fraction())

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
    split_from.SetValue(GncNumeric(amount, curr.get_fraction()))
    split_from.SetAmount(GncNumeric(amount, curr.get_fraction()))

    split_to = Split(book)
    split_to.SetParent(tx)
    split_to.SetAccount(acc_to)
    split_to.SetValue(GncNumeric(amount, curr.get_fraction()))
    split_to.SetAmount(GncNumeric(amount, curr.get_fraction()))

    tx.CommitEdit()
    
def write_to_gnucash_file():
    print "TODO stub: Writing to GNUCash file"

def stub():
    print "Just a stub method..."
