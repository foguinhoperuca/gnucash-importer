import gnucash_importer
from gnucash_importer.util import Util
from gnucash_importer.account import Nubank
from gnucash_importer.ledger import Ledger
import unittest

# from gnucash import Session, Transaction, Split, GncNumeric, gnucash_core_c

class TestLedger(unittest.TestCase):
    def setUp(self):
        self.util = Util()
        self.account = Nubank('example/local/nubank-2016-10.ofx')
        self.ledger = Ledger(self.account, self.util.DEFAULT_CURRENCY, False, self.util.DEFAULT_GNUCASH_FILE)

    # TODO implement catch exception
    def test_get_quantity_transactions(self): # only happy case
        # initial quantity
        self.assertEqual(self.ledger.get_quantity_transactions(), 36)

        # after commit some transactions
        self.ledger.write()
        self.assertEqual(self.ledger.get_quantity_transactions(), 45)

    @unittest.skip("not implemented yet!")
    def test_get_gnucash_currency(self):
        book = None             # TODO implement setUp to get book information
        currency = self.ledger.get_gnucas_currency(book, self.util.DEFAULT_CURRENCY)
        self.assertEqual('BRL', currency)

    @unittest.skip("not implemented yet!")
    def test_write(self):
        self.assertTrue(True)
        # self.ledger.write()

if __name__ == '__main__':
    unittest.main()
