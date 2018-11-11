# -*- coding: utf-8 -*-

'''
Module to read all file formats that will be supported
'''

import logging
from ofxparse import OfxParser  # ofxparse 0.14+

class EntryReader:
    def get_transaction(report_file):
        pass

    def print_transaction(transaction):
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        # print(transaction)
        print("amount): %s" % (transaction.amount))
        print("checknum): %s" % (transaction.checknum))
        print("date): %s" % (transaction.date))
        print("id): %s" % (transaction.id))
        print("mcc): %s" % (transaction.mcc))
        print("memo): %s" % (transaction.memo.encode('iso-8859-1')))
        print("payee): %s" % (transaction.payee))
        print("sic): %s" % (transaction.sic))
        print("type): %s" % (transaction.type))
        print("------------------------------------------------------------")

class OfxReader(EntryReader):
    def get_transactions(report_file):
        print("TODO stub method")
        ofx = OfxParser.parse(file(report_file))

        for transaction in ofx.account.statement.transactions:
            print_transaction(transaction)

        return ofx.account.statement.transactions

class QifReader(EntryReader):
    def get_transactions(report_file):
        print("TODO stub method")

class CsvReader(EntryReader):
    def get_transactions(report_file):
        print("TODO stub method")
