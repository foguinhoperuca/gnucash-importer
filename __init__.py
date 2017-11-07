#!/usr/bin/env python

import uuid
import argparse
import logging

# gather the uuid frm kernel...
# uuid = open('/proc/sys/kernel/random/uuid', 'r')
# print str(uuid.uuid4())

def get_args():
    parser = argparse.ArgumentParser(description = "GNUCash utility to fix xml file and import custom data.")
    parser.add_argument("-q", "--quiet", action='store_true', help="Set *NO* verbose logging i.e.: loglevel = logging.WARN")
    parser.add_argument("-v", "--verbose", action='store_true', help="Set *VERBOSE* logging i.e.: loglevel = logging.DEBUG")
    # parser.add_argument("gnucash_file", help="GNUCash xml file")
    args = parser.parse_args()

    return args

def main():
    args = get_args()
    if args.verbose:
        loglevel = logging.DEBUG
    elif args.quiet:
        loglevel = logging.WARN
    else:
        loglevel = logging.INFO

    print 'loglevel is: '
    print loglevel
    
    print 'bye!!'

if __name__ == "__main__":
    main()
