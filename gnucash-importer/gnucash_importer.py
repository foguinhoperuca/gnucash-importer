#!/usr/bin/env python3

import logging
from ledger import Ledger
from account import Nubank, CashInWallet, CefSavingsAccount, ItauCheckingAccount, ItauSavingsAccount, BradescoSavingsAccount
from util import Util

def main(args):
    if args.verbose:
        loglevel = logging.DEBUG
        logformat = Util.LOG_FORMAT_DEBUG
    elif args.quiet:
        loglevel = logging.WARN
        # TODO log to file in this case
        logformat = Util.LOG_FORMAT_FULL
    else:
        loglevel = logging.INFO
        logformat = Util.LOG_FORMAT_SIMPLE

    # TODO config logger by dictnoray - https://realpython.com/python-logging/
    logging.basicConfig(level = loglevel, format = logformat)

    if args.verbose:
        logging.debug(Util.debug("ARGS:"))
        logging.debug(Util.debug(args))
        logging.debug(Util.debug(args.dry_run))
        logging.debug(Util.debug(loglevel))
        logging.debug(Util.debug(args.currency))
        logging.debug(Util.debug(args.gnucash_file))
        logging.debug(Util.debug(args.account))
        logging.debug(Util.debug(args.account_src_file))
    
    account = {
        "nubank": Nubank(args.account_src_file),
        "ciw": CashInWallet(args.account_src_file),
        "cef-savings": CefSavingsAccount(args.account_src_file),
        "itau-cc": ItauCheckingAccount(args.account_src_file),
        "itau-savings": ItauSavingsAccount(args.account_src_file),
        "bradesco-savings": BradescoSavingsAccount(args.account_src_file)
    }.get(args.account, None)

    if account is None:
        raise Exception("Failed with account: need be defined!!!")

    ledger = Ledger(account, args.currency, args.dry_run, args.gnucash_file)
    ledger.write()
