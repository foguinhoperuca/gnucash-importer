#!/usr/bin/env python

import logging
import argparse
import configparser

# GNUCash interface
import gnucash_interface
# from gnucash_interface import write_to_gnucash_file
import read_entry
import account
from util import Util

def read_nubank(ofx_file):
    print 'Reading Nubank data from .ofx!!'

def main(args):
    if args.verbose:
        loglevel = logging.DEBUG
    elif args.quiet:
        loglevel = logging.WARN
    else:
        loglevel = logging.INFO

    logging.basicConfig(level = loglevel)

    if args.gnucash_file is None:
        file_path = nubank.ofx
    else:
        file_path = args.gnucash_file

    if args.account_src is None:
        account_src = ""
    else:
        account_src = args.account_src

    read_nubank(file_path)

    print "ARGS:"
    print args.gnucash_file
    print args.account_src
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "GNUCash utility to fix xml file and import custom data.")
    parser.add_argument("-q", "--quiet", action = 'store_true', help = "Set *NO* verbose logging i.e.: loglevel = logging.WARN")
    parser.add_argument("-v", "--verbose", action = 'store_true', help = "Set *VERBOSE* logging i.e.: loglevel = logging.DEBUG")
    parser.add_argument("gnucash_file", help = "GNUCash xml file")
    parser.add_argument("account_src", help = "Set account source to integrate")

    # TODO pass config as an argument to main or use directly?
    config = configparser.ConfigParser()
    config.read('setup.cfg')
    
    main(parser.parse_args())
