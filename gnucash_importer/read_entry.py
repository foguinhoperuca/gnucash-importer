# -*- coding: utf-8 -*-

"""
Module to read all file formats that will be supported
"""
import logging
from ofxparse import OfxParser  # ofxparse 0.14+

class EntryReader(object):
    transactions = None

    def __init__(self):
        pass

    def get_transaction(self, report_file):
        pass

    def print_transactions(self):
        for transaction in self.transactions:
            self.print_transaction(transaction)
    
    def print_transaction(self, transaction):
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("amount....: %s" % (transaction.amount))
        print("checknum..: %s" % (transaction.checknum))
        print("date......: %s" % (transaction.date))
        print("id........: %s" % (transaction.id))
        print("mcc.......: %s" % (transaction.mcc))
        print("memo......: %s" % (transaction.memo.encode('iso-8859-1')))
        print("payee.....: %s" % (transaction.payee))
        print("sic.......: %s" % (transaction.sic))
        print("type......: %s" % (transaction.type))

class OfxReader(EntryReader):
    def get_transactions(self, report_file):
        report = open(report_file)
        ofx = OfxParser.parse(report)
        self.transactions = ofx.account.statement.transactions
        report.close()

        return self.transactions

class QifReader(EntryReader):
    def get_transactions(self, report_file):
        print("TODO stub method")

class CsvReader(EntryReader):
    def get_transactions(self, report_file):
        print("TODO stub method")
