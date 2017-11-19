#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Meant to be reuseable interface with gnucash
'''

import logging
import datetime
from Decimal import decimal
from gnucash import Session, Transaction, Split, GncNumeric

def get_currency(book, curr = default_currency):
    commod_tab = book.get_table()
    currency = commod_tab.lookup('ISO4217', curr)

# Extracted from https://github.com/hjacobs/gnucash-qif-import/blob/master/import.py#lookup_account_by_path(root, path)
def get_account_by_path(root, path):
    acc = root.lookup_by_name(path[0])

    if acc.get_instance() == None:
        raise Exception('NO Good: account path not found --> %s' % (path[0]))

    if len(path) > 1:
        get_account_by_path(acc, path[1:])

    return acc

def get_account(book, acc_name):
    get_account_by_path(book.get_root_account(), acc_name.split(':'))

def create_gnucash_tansaction(book, item, curr, account_from = assets_account_path, account_to = blackhole_account_path):
    if curr is None:
        curr = get_currency(book, default_currency)

    if item is None:
        raise Exception("Could not create a gnucash transaction: missing item!!")

    if book is None:
        raise Exception("Could not create a gnucash transaction: missing book!!")

    acc_from = get_account(book, account_from)
    acc_to = get_account(book, account_to)
    amount = int(Decimal(item.split_amount.replace(',', '.')) * curr.get_fraction())
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

# FIXME receive items or gnucash transaction?
def write_to_gnucash_file(dry_run = True, gnucash_file = default_gnucash_file, items, curr = default_currency, account_from, account_to):
    sess = Session(gnucash_file)
    book = sess.book
    currency = get_currency(book, curr)

    imported_items = set()
    for item in items:
        if item.as_tuple() in imported_items:
            logging.info("Skipped because it already was imported!!!")
            continue

        create_gnucash_tansaction(book, item, currency, account_from, account_to):
        imported_items.add(item.as_tuple())

    if dry_run:
        logging.info('############### DRY-RUN ###############')
    else:
        logging.info('Saving GNUCash file..')
        session.save()

    session.end()

def stub():
    print "Just a stub method..."
