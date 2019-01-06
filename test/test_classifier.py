import unittest
import gnucash_importer
from gnucash_importer.util import Util
from gnucash_importer.ledger import Ledger
from gnucash_importer.classifier import Classifier, Strategy, SupplierStrategy
import unittest
from gnucash import Session, GncCommodity

class ClassifierTestCase(unittest.TestCase):
    def setUp(self):
        self.util = Util()
        self.ledger = Ledger()
        session = Session(self.util.DEFAULT_GNUCASH_FILE)
        self.book = session.book
        self.currency = self.book.get_table().lookup('ISO4217', self.util.DEFAULT_CURRENCY) # FIXME need it?
        session.end()


    def test_init_classifier(self):
        classifier = Classifier("SupplierStrategy")
        self.assertEqual("SupplierStrategy", classifier.strategy)

        with self.assertRaises(ValueError) as context:
            Classifier(None)
        self.assertTrue("strategy can't be None! Please, inform the strategy that should be utilized to classify a transaction!", context.exception)

        with self.assertRaises(ValueError) as context:
            Classifier("NOT_AVAILABLE_STRATEGY")
        self.assertTrue("strategy must be valid! Please, inform a valid strategy from ({s}) that should be utilized to classify a transaction!".format(s = Classifier.AVAILABLE_STRATEGIES), context.exception)
        

    @unittest.skip("TODO implement it!")
    def test_validate_strategy(self):
        assertTrue(True)
        # def validate_strategy(strategy = _strategy):

    @unittest.skip("TODO implement it!")
    def test_classify_split(self):
        # def classify_split(split, strategy = _strategy):
        assertTrue(True)

    @unittest.skip("TODO implement it!")
    def test_validate_split(account):
        assertTrue(True)

    @unittest.skip("TODO implement it!")
    def test_classify(split):
        assertTrue(True)
        # def classify(split, gnuash_book)

        # # FIXME need mannually use this code before real test!!!!
        # gnucash_acc_to = self.get_gnucash_account(gnucash_book, self.account.acc_to)
        # amount = int(Decimal(item.amount) * gnucash_currency.get_fraction())
        # tx = Transaction(gnucash_book)
        # tx.BeginEdit()
        # tx.SetCurrency(gnucash_currency)
        # tx.SetDescription(item.memo)
        # tx.SetDateEnteredSecs(datetime.datetime.now())
        # tx.SetDatePostedSecs(item.date)

        # TODO get a invalid account
        tx = Transaction(self.book)
        tx.BeginEdit()
        tx.SetDescription(item.memo)
        supplier_not_found = SupplierStrategy()
        assertEqual(self.util.DEFAULT_NUBANK_TO, supplier_not_found.classify()) # FIXME parse it back to string

        # TODO get a valid account
        tx = Transaction(self.book)
        tx.BeginEdit()
        tx.SetDescription(item.memo)
        supplier_found = SupplierStrategy()
        assertEqual("", supplier_found.classify()) # FIXME parse it back to string
