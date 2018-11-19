#!/usr/bin/env python

import os
from util import Util
from read_entry import OfxReader
from read_entry import QifReader
from read_entry import CsvReader

class Account(object):
    _acc_from = None
    _acc_to = None
    _account_src_file = None

    def __init__(self, acc_from, acc_to, acc_src_file):
        self._acc_from = acc_from
        self._to = acc_to
        self._account_src_file = acc_src_file

    def __init__(self, acc_src_file):
        self._account_src_file = acc_src_file

    @property
    def acc_from(self):
        return self._acc_from
    @acc_from.setter
    def acc_from(self, value):
        self._acc_from = value
    @acc_from.deleter
    def acc_from(self):
        del self._acc_from

    @property
    def acc_to(self):
        return self._acc_to
    @acc_to.setter
    def acc_to(self, value):
        self._acc_to = value
    @acc_to.deleter
    def acc_to(self):
        del self._acc_to

    @property
    def account_src_file(self):
        return self._account_src_file
    @account_src_file.setter
    def account_src_file(self, value):
        self._account_src_file = value
    @account_src_file.deleter
    def account_src_file(self):
        del self._account_src_file

    def get_items(self):
        file_type = os.path.splitext(self.account_src_file)[1]

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
        self.acc_from = Util().DEFAULT_NUBANK_FROM
        self.acc_to = Util().DEFAULT_NUBANK_TO

class CashInWallet(Account):
    def __init__(self, acc_src_file):
        super(CashInWallet, self).__init__(acc_src_file)
        self.acc_from = Util().DEFAULT_CIW_FROM
        self.acc_to = Util().DEFAULT_CIW_TO

class CefSavingsAccount(Account):
    def __init__(self, acc_src_file):
        super(CefSavingsAccount, self).__init__(acc_src_file)
        self.acc_from = Util().DEFAULT_CEF_SAVINGS_FROM
        self.acc_to = Util().DEFAULT_CEF_SAVINGS_TO

class ItauCheckingAccount(Account):
    def __init__(self, acc_src_file):
        super(ItauCheckingAccount, self).__init__(acc_src_file)
        self.acc_from = Util().DEFAULT_ITAU_CHECKING_ACCOUNT_FROM
        self.acc_to = Util().DEFAULT_ITAU_CHECKING_ACCOUNT_TO

class ItauSavingsAccount(Account):
    def __init__(self, acc_src_file):
        super(ItauSavingsAccount, self).__init__(acc_src_file)
        self.acc_from = Util().DEFAULT_ITAU_SAVINGS_FROM
        self.acc_to = Util().DEFAULT_ITAU_SAVINGS_TO

class BradescoSavingsAccount(Account):
    def __init__(self, acc_src_file):
        super(BradescoSavingsAccount, self).__init__(acc_src_file)
        self.acc_from = Util().DEFAULT_BRADESCO_SAVINGS_FROM
        self.acc_to = Util().DEFAULT_BRADESCO_SAVINGS_TO
