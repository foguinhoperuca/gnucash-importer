# FIXME can't import classes to test....
# import sys
# sys.path.append('../gnucash_importer')
import gnucash_importer
from gnucash_importer.util import Util
from gnucash_importer.account import Nubank
from gnucash_importer.ledger import Ledger
import unittest

class TestLedger(unittest.TestCase):
    def setUp(self):
        self.util = Util()
        self.account = Nubank('example/local/nubank-2016-10.ofx')
        self.ledger = Ledger(self.account, self.util.DEFAULT_CURRENCY, False, self.util.DEFAULT_GNUCASH_FILE)

    def test_get_gnucash_currency(self):
        # def get_gnucash_currency(self, book, curr = 'BRL'):
        self.assertTrue(True)
        self.ledger.write()

if __name__ == '__main__':
    unittest.main()
