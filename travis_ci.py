import sys
import pprint

sys.path.append('/usr/lib/python3/dist-packages/')

print("------------------------")
# print(help('modules'))
pprint.pprint(sys.path)
print("------------------------")

from gnucash import Session, Transaction, Split, GncNumeric
