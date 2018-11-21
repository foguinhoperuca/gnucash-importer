import gnucash_importer
from gnucash_importer.util import Util
from gnucash_importer.account import Nubank
from gnucash_importer.ledger import Ledger
import unittest

# from gnucash import Session, Transaction, Split, GncNumeric, gnucash_core_c
import xml.etree.ElementTree as ET

class TestLedger(unittest.TestCase):
    def setUp(self):
        self.util = Util()
        self.account = Nubank('example/local/nubank-2016-10.ofx')
        self.ledger = Ledger(self.account, self.util.DEFAULT_CURRENCY, False, self.util.DEFAULT_GNUCASH_FILE)

        # FIXME can't get count_transactions
        # print("self.util.DEFAULT_GNUCASH_FILE: {d}".format(d = self.util.DEFAULT_GNUCASH_FILE))
        # session = Session(self.util.DEFAULT_GNUCASH_FILE)
        # gnucash_book = session.book
        # Util.show_methods(gnucash_book)
        # Util.show_methods(gnucash_core_c.gnc_book_count_transactions)
        # print(gnucash_core_c.gnc_book_count_transactions(session.book))
        # print(gnucash_core_c.gnc_book_count_transactions(gnucash_book)')

        # TODO implement Manual count gnucash transactions...
        # <gnc:count-data cd:type="transaction">45</gnc:count-data>
        tree = ET.parse(self.util.DEFAULT_GNUCASH_FILE)
        root = tree.getroot()
        
        print(root.tag)
        print(root.attrib)
        
        for child in root:
            print("tag: {t}".format(t = child.tag))
            print("attrib: {a}".format(a = child.attrib))

        print("+++++++++++++++++")
        for x in root.iter('count-data'):
            print(x.attrib)

        # for node in tree.findall('gnc:book'):
        #     print("inside tree...")
        #     url = node.attrib.get('xmlUrl')
        #     if url:
        #         print(url)

    def test_get_gnucash_currency(self):
        # def get_gnucash_currency(self, book, curr = 'BRL'):
        self.assertTrue(True)
        # self.ledger.write()

if __name__ == '__main__':
    unittest.main()
