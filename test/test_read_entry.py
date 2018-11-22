from gnucash_importer.read_entry import OfxReader, QifReader, CsvReader
import unittest

class EntryReaderTestCase(unittest.TestCase):
    # FIXME create a fixture for this test (example/local/nubank-2016-10.ofx is private file)
    def test_get_transactions_ofx(self):
        transactions = OfxReader().get_transactions("example/local/nubank-2016-10.ofx")
        self.assertEqual(len(transactions), 9)

    @unittest.skip("not implemented yet")
    def test_get_transactions_qif(self):
        pass

    @unittest.skip("not implemented yet")
    def test_get_transactions_csv(self):
        pass
        
if __name__ == '__main__':
    unittest.main()
