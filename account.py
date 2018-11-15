#!/usr/bin/env python

import logging
from util import Util
from read_entry import OfxReader
from read_entry import QifReader
from read_entry import CsvReader

class Account(object):
    acc_from = None
    to = None
    account_src_file = None
    
    def __init__(self, acc_from, acc_to, acc_src_file):
        self.acc_from = acc_from
        self.to = acc_to
        self.account_src_file = acc_src_file

    def __init__(self, acc_src_file):
        self.account_src_file = acc_src_file

    def get_items(self, file_type, account_file):
        if account_file is None:
            acc_src = self.account_src_file

        if file_type is None:
            file_type = "ofx"

        if file_type == "qif":
            return QifReader().get_transactions(self.account_src_file)
        elif file_type == "csv":
            return CsvReader().get_transactions(self.account_src_file)
        else:
            return OfxReader().get_transactions(self.account_src_file)

# for every source account do:
class Nubank(Account):
    def __init__(self, acc_src_file):
        super(Nubank, self).__init__(acc_src_file)
        self.account_from = Util().DEFAULT_NUBANK_FROM
        self.to = Util().DEFAULT_NUBANK_TO

class CashInWallet(Account):
    def __init__(self, acc_src_file):
        super(CashInWallet, self).__init__(acc_src_file)
        self.account_from = Util().DEFAULT_CIW_FROM
        self.to = Util().DEFAULT_CIW_TO

class CefSavingsAccount(Account):
    def __init__(self, acc_src_file):
        super(CefSavingsAccount, self).__init__(acc_src_file)
        self.account_from = Util().DEFAULT_CEF_SAVINGS_FROM
        self.to = Util().DEFAULT_CEF_SAVINGS_TO

class ItauCheckingAccount(Account):
    def __init__(self, acc_src_file):
        super(ItauCheckingAccount, self).__init__(acc_src_file)
        self.account_from = Util().DEFAULT_ITAU_CHECKING_ACCOUNT_FROM
        self.to = Util().DEFAULT_ITAU_CHECKING_ACCOUNT_TO

class ItauSavingsAccount(Account):
    def __init__(self, acc_src_file):
        super(ItauSavingsAccount, self).__init__(acc_src_file)
        self.account_from = Util().DEFAULT_ITAU_SAVINGS_FROM
        self.to = Util().DEFAULT_ITAU_SAVINGS_TO

class BradescoSavingsAccount(Account):
    def __init__(self, acc_src_file):
        super(BradescoSavingsAccount, self).__init__(acc_src_file)
        self.account_from = Util().DEFAULT_BRADESCO_SAVINGS_FROM
        self.to = Util().DEFAULT_BRADESCO_SAVINGS_TO
