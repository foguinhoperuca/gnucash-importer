# -*- coding: utf-8 -*-

import configparser

class Util:
    config = configparser.ConfigParser()
    DEFAULT_CURRENCY = None
    DEFAULT_GNUCASH_FILE = None

    def __init__(self):
        self.config.read('setup.cfg')
        self.DEFAULT_CURRENCY = self.config['bdist_wheel']['default_currency']
        self.DEFAULT_GNUCASH_FILE = self.config['bdist_wheel']['default_gnucash_file']
