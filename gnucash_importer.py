#!/usr/bin/env python

import uuid
import argparse
import logging

# ofxparse 0.14+
from ofxparse import OfxParser

# GNUCash interface
import gnucash_interface
# from gnucash_interface import write_to_gnucash_file
import read_entry
import account

def read_nubank(ofx_file):
    print 'Reading Nubank data from .ofx!!'

    ofx = OfxParser.parse(file(ofx_file))

    # for transaction in ofx.account.statement.transactions:
    #     print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
    #     # print dir(transaction)
    #     print "amount: %s" % (transaction.amount)
    #     print "checknum: %s" % (transaction.checknum)
    #     print "date: %s" % (transaction.date)
    #     print "id: %s" % (transaction.id)
    #     print "mcc: %s" % (transaction.mcc)
    #     print "memo: %s" % (transaction.memo.encode('iso-8859-1'))
    #     print "payee: %s" % (transaction.payee)
    #     print "sic: %s" % (transaction.sic)
    #     print "type: %s" % (transaction.type)
    #     print "------------------------------------------------------------"
    #     # create_gnucash_tansaction()        

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


    read_nubank(file_path)
    # gnucash_interface.write_to_gnucash_file()

    gnucash_interface.stub()
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "GNUCash utility to fix xml file and import custom data.")
    parser.add_argument("-q", "--quiet", action='store_true', help="Set *NO* verbose logging i.e.: loglevel = logging.WARN")
    parser.add_argument("-v", "--verbose", action='store_true', help="Set *VERBOSE* logging i.e.: loglevel = logging.DEBUG")
    parser.add_argument("gnucash_file", help="GNUCash xml file")
    
    main(parser.parse_args())
