import sys
import pprint

sys.path.append('/usr/lib/python3/dist-packages/')

print("------------------------")
# print(help('modules'))
pprint.pprint(sys.path)
print("------------------------")

from gnucash import Session, Transaction, Split, GncNumeric



# /usr/lib/python3/dist-packages/gnucash
# /usr/lib/python3/dist-packages/gnucash/_gnucash_core_c.cpython-36m-x86_64-linux-gnu.so
# /usr/lib/python3/dist-packages/gnucash/__pycache__/gnucash_business.cpython-35.pyc
# /usr/lib/python3/dist-packages/gnucash/__pycache__/gnucash_core_c.cpython-35.pyc
# /usr/lib/python3/dist-packages/gnucash/__pycache__/gnucash_core.cpython-35.pyc
# /usr/lib/python3/dist-packages/gnucash/gnucash_core_c.py
# /usr/lib/python3/dist-packages/gnucash/gnucash_core.py
# /usr/lib/python3/dist-packages/gnucash/gnucash_business.py
