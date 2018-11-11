#!/usr/bin/env python3

import logging
import argparse
import configparser

# GNUCash interface
import gnucash_interface
# from gnucash_interface import write_to_gnucash_file
import read_entry
from account import *
from util import Util

def main(args):
    if args.verbose:
        loglevel = logging.DEBUG
        print("ARGS:")
        print(args)
        print(args.dry_run)
        print(loglevel)
        print(args.currency)
        print(args.gnucash_file)
        print(args.account)
        print(args.account_src_file)
        print("-------------------------------------------------------")
    elif args.quiet:
        loglevel = logging.WARN
    else:
        loglevel = logging.INFO

    logging.basicConfig(level = loglevel)
    
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

    if args.verbose:
        print(account)
        print(account.account_from)
        print(account.to)
        print(account.account_src_file)
        print("-------------------------------------------------------")

    gnucash_interface.write_to_gnucash_file(account, args.dry_run, args.gnucash_file, args.currency)

# Basic command: python3 gnucash_importer.py -gf example/test_ledger.gnucash -a nubank -af example/local/nubank-2016-10.ofx -dr -v
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "GNUCash utility to fix xml file and import custom data.")
    parser.add_argument("-dr", "--dry-run", action = 'store_true', help = "actions will *NOT* be writen to gnucash file.")
    parser.add_argument("-q", "--quiet", action = 'store_true', help = "Set *NO* verbose logging i.e.: loglevel = logging.WARN")
    parser.add_argument("-v", "--verbose", action = 'store_true', help = "Set *VERBOSE* logging i.e.: loglevel = logging.DEBUG")
    parser.add_argument("-c", "--currency", default = Util().DEFAULT_CURRENCY, help = "currency used in gnucash. Default is BRL.")
    parser.add_argument("-gf", "--gnucash_file", default = Util().DEFAULT_GNUCASH_FILE, help = "GNUCash xml file to write")
    parser.add_argument("-a", "--account", choices = ["nubank", "ciw", "cef-savings", "itau-cc", "itau-savings", "bradesco-savings"], required = True, help = "Set account that will be used.")
    parser.add_argument("-af", "--account_src_file", required = True, help = "Set account source to integrate")

    main(parser.parse_args())
