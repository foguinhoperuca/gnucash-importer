# -*- coding: utf-8 -*-
"""
Util module to concetrate all reusable code.

This modules support all other classes/modules with usefull source code that doesn't belong to any other entity.
"""

import configparser
import logging
from termcolor import colored, cprint

class Util:
    """Helper class used to provide configuration, defaults and so on."""
    config = configparser.ConfigParser()
    LOG_FORMAT_FULL = colored('[%(asctime)s][%(process)d:%(processName)s]', 'green', attrs=['bold', 'dark']) + colored('[%(filename)s#%(funcName)s:%(lineno)d]', 'white', attrs=['bold', 'dark']) + colored('[%(levelname)s]', 'magenta', attrs=['bold', 'dark']) + ' %(message)s'
    LOG_FORMAT_DEBUG = colored('[%(filename)s#%(funcName)s:%(lineno)d]', 'white', attrs=['bold', 'dark']) + colored('[%(levelname)s]', 'magenta', attrs=['bold', 'dark']) + ' %(message)s'
    LOG_FORMAT_SIMPLE = colored('[%(levelname)s]', 'magenta', attrs=['bold', 'dark']) + ' %(message)s'
    DEFAULT_CURRENCY = None
    DEFAULT_GNUCASH_FILE = None
    DEFAULT_ACCOUNT_SRC_FILE = None
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
        """Grab all configuration in setup.cfg"""
        self.config.read('setup.cfg')
        self.DEFAULT_CURRENCY = self.config['app_init']['default_currency']
        self.DEFAULT_GNUCASH_FILE = self.config['app_init']['default_gnucash_file']
        self.DEFAULT_ACCOUNT_SRC_FILE = self.config['app_init']['default_account_src_file']
        self.DEFAULT_NUBANK_TO = self.config['app_init']['default_nubank_to']
        self.DEFAULT_NUBANK_FROM = self.config['app_init']['default_nubank_from']
        self.DEFAULT_CIW_TO = self.config['app_init']['default_ciw_to']
        self.DEFAULT_CIW_FROM = self.config['app_init']['default_ciw_from']
        self.DEFAULT_CEF_SAVINGS_TO = self.config['app_init']['default_cef_savings_to']
        self.DEFAULT_CEF_SAVINGS_FROM = self.config['app_init']['default_cef_savings_from']
        self.DEFAULT_ITAU_CHECKING_ACCOUNT_TO = self.config['app_init']['default_itau_checking_account_to']
        self.DEFAULT_ITAU_CHECKING_ACCOUNT_FROM = self.config['app_init']['default_itau_checking_account_from']
        self.DEFAULT_ITAU_SAVINGS_TO = self.config['app_init']['default_itau_savings_to']
        self.DEFAULT_ITAU_SAVINGS_FROM = self.config['app_init']['default_itau_savings_from']
        self.DEFAULT_BRADESCO_SAVINGS_TO = self.config['app_init']['default_bradesco_savings_to']
        self.DEFAULT_BRADESCO_SAVINGS_FROM = self.config['app_init']['default_bradesco_savings_from']

    def show_methods(obj):
        """Helper to discovery API of an object."""
        logging.basicConfig(level = logging.DEBUG, format = Util.LOG_FORMAT_DEBUG)
        logging.debug(colored("_______________________________________________________", 'cyan'))
        logging.debug(colored("type(obj)..: {t}".format(t = type(obj)), 'cyan'))
        logging.debug(colored("vars(obj)..: {v}".format(v = vars(obj)), 'cyan'))
        logging.debug(colored("dir(obj)...: {d}".format(d = dir(obj)), 'cyan'))
        for method in [method_name for method_name in dir(obj) if callable(getattr(obj, method_name))]:
            print(method)
        help(obj)
        logging.debug(colored("_______________________________________________________", 'cyan'))

    def info(msg):
        """This function standardize the message and simplified the use to standard output."""
        return colored(msg, 'blue')

    def warning(msg):
        """This function standardize the message and simplified the use to standard output."""
        return colored(msg, 'yellow', attrs=['bold'])

    def error(msg):
        """This function standardize the message and simplified the use to standard output."""
        return colored(msg, 'red', attrs=['bold', 'underline'])

    def debug(msg):
        """This function standardize the message and simplified the use to standard output."""
        return colored(msg, 'grey', attrs=['reverse', 'bold', 'underline'])
