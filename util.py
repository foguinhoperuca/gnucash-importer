# -*- coding: utf-8 -*-

import configparser

class Util:
    config = configparser.ConfigParser()
    DEFAULT_CURRENCY = None
    DEFAULT_GNUCASH_FILE = None
    DEFAULT_NUBANK_TO = None
    DEFAULT_NUBANK_FROM = None
    DEFAULT_CIW_TO = None
    DEFAULT_CIW_FROM = None
    DEFAULT_CEF_SAVINGS_TO = None
    DEFAULT_CEF_SAVINGS_FROM = None
    DEFAULT_ITAU_CHECKING_ACCOUNT_TO = None
    DEFAULT_ITAU_CHECKING_ACCOUNT_FROM = None
    DEFAULT_ITAU_SAVINGS_TO = None
    DEFAULT_ITAU_SAVINGS_FROM = None
    DEFAULT_BRADESCO_SAVINGS_TO = None
    DEFAULT_BRADESCO_SAVINGS_FROM = None

    def __init__(self):
        self.config.read('setup.cfg')
        self.DEFAULT_CURRENCY = self.config['bdist_wheel']['default_currency']
        self.DEFAULT_GNUCASH_FILE = self.config['bdist_wheel']['default_gnucash_file']
        self.DEFAULT_NUBANK_TO = self.config['bdist_wheel']['default_nubank_to']
        self.DEFAULT_NUBANK_FROM = self.config['bdist_wheel']['default_nubank_from']
        self.DEFAULT_CIW_TO = self.config['bdist_wheel']['default_ciw_to']
        self.DEFAULT_CIW_FROM = self.config['bdist_wheel']['default_ciw_from']
        self.DEFAULT_CEF_SAVINGS_TO = self.config['bdist_wheel']['default_cef_savings_to']
        self.DEFAULT_CEF_SAVINGS_FROM = self.config['bdist_wheel']['default_cef_savings_from']
        self.DEFAULT_ITAU_CHECKING_ACCOUNT_TO = self.config['bdist_wheel']['default_itau_checking_account_to']
        self.DEFAULT_ITAU_CHECKING_ACCOUNT_FROM = self.config['bdist_wheel']['default_itau_checking_account_from']
        self.DEFAULT_ITAU_SAVINGS_TO = self.config['bdist_wheel']['default_itau_savings_to']
        self.DEFAULT_ITAU_SAVINGS_FROM = self.config['bdist_wheel']['default_itau_savings_from']
        self.DEFAULT_BRADESCO_SAVINGS_TO = self.config['bdist_wheel']['default_bradesco_savings_to']
        self.DEFAULT_BRADESCO_SAVINGS_FROM = self.config['bdist_wheel']['default_bradesco_savings_from']
