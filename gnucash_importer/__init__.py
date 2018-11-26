import logging
import argparse
from cli import Cli
from util import Util
from ledger import Ledger
from read_entry import OfxReader, QifReader, CsvReader
from account import GenericAccount, Nubank, CashInWallet, CefSavingsAccount, ItauCheckingAccount, ItauSavingsAccount, BradescoSavingsAccount

name = "gnucash_importer"
__all__ = ["account", "cli", "ledger", "ncurses", "red_entry", "util"] # TODO verify what that's meaning

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "GNUCash utility to fix xml file and import custom data.")
    parser.add_argument("-dr", "--dry-run", action = 'store_true', help = "actions will *NOT* be writen to gnucash file.")
    parser.add_argument("-q", "--quiet", action = 'store_true', help = "Set *NO* verbose logging i.e.: loglevel = logging.WARN")
    parser.add_argument("-v", "--verbose", action = 'store_true', help = "Set *VERBOSE* logging i.e.: loglevel = logging.DEBUG")
    parser.add_argument("-c", "--currency", default = Util().DEFAULT_CURRENCY, help = "currency used in gnucash. Default is BRL.")
    parser.add_argument("-gf", "--gnucash_file", default = Util().DEFAULT_GNUCASH_FILE, help = "GNUCash xml file to write")
    parser.add_argument("-a", "--account", choices = ["nubank", "ciw", "cef-savings", "itau-cc", "itau-savings", "bradesco-savings", "generic"], required = True, help = "Set account that will be used.")
    parser.add_argument("-af", "--account_src_file", required = True, help = "Set account source to integrate")
    parser.add_argument("-acf", "--account_from", help = "Define from import")
    parser.add_argument("-act", "--account_to", help = "Define to import")

    args = parser.parse_args()
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
    }.get(args.account, GenericAccount(args.account_from, args.account_to, args.account_src_file))

    logging.debug(Util.debug(vars(account)))

    if account is None:
        raise Exception("Failed with account: need be defined!!!")


    Cli.import_data(account, args.currency, args.dry_run, args.gnucash_file)
