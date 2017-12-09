#!/usr/bin/env python

import logging

class Account():
    def __init__(self, acc_from, acc_to, acc_src_file):
        self.acc_from = acc_from
        self.to = acc_to
        self.account_src_file = acc_src_file

    def __init__(self, acc_src_file):
        self.account_src_file = acc_src_file

    def get_items(file_type, account_file):
        if account_file is None:
            acc_src = self.account_src_file

        return {
            "ofx": OfxReader.get_transactions(acc_src),
            "qif": QifReader.get_transactions(acc_src),
            "csv": CsvReader.get_transactions(acc_src),
        }.get(file_type, "ofx")

# for every source account do:
class Nubank(Account):
    def __init__(self, acc_src_file):
        super(Nubank).__init__(self, acc_src_file)
        self.account_from = "NUBANK_FROM"
        self.to = "NUBANK_TO"

class CashInWallet(Account):
    def __init__(self, acc_src_file):
        super(CashinWallet).__init__(self, acc_src_file)
        self.account_from = "CIW_FROM"
        self.to = "CIW_TO"

class CefSavingsAccount(Account):
    def __init__(self, acc_src_file):
        super(CefSavingsAccount).__init__(self, acc_src_file)
        self.account_from = "CEF_FROM"
        self.to = "CEF_TO"

class ItauCheckingAccount(Account):
    def __init__(self, acc_src_file):
        super(ItauCheckingAccount).__init__(self, acc_src_file)
        self.account_from = "ITAUCC_FROM"
        self.to = "ITAUCC_TO"

class ItauSavingsAccount(Account):
    def __init__(self, acc_src_file):
        super(ItauSavingsAccount).__init__(self, acc_src_file)
        self.account_from = "ITAUSAVINGS_FROM"
        self.to = "ITAUSAVINGS_TO"

class BradescoSavingsAccount(Account):
    def __init__(self, acc_src_file):
        super(BradescoSavingsAccount).__init__(self, acc_src_file)
        self.account_from = "BRADESCO_FROM"
        self.to = "BRADESCO_TO"
