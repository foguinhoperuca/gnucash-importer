#!/usr/bin/env python3

import logging
from termcolor import colored
from util import Util
from ledger import Ledger

"""
This class will coordinate all actions
"""
class Cli:
    def import_data(account, currency, dry_run, gnucash_file):
        logging.info(Util.info("Importing data to ")  + colored("{a}".format(a = account.name), 'yellow', attrs=['bold', 'underline']) + Util.info("'s account"))
        Ledger(account, currency, dry_run, gnucash_file).write()
        # TODO implement report
