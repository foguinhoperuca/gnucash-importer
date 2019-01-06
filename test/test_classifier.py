import unittest
import gnucash_importer
from gnucash_importer.util import Util
from gnucash_importer.classifier import Classifier, Strategy, SupplierStrategy
import unittest
from gnucash import Session, Transaction, GncCommodity

class ClassifierTestCase(unittest.TestCase):
    def setUp(self):
        self.util = Util()
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
        pass
        # def validate_strategy(strategy = _strategy):

    @unittest.skip("TODO implement it!")
    def test_classify_split(self):
        # def classify_split(split, strategy = _strategy):
        pass

    @unittest.skip("TODO implement it!")
    def test_validate_split(self):
        pass

    def test_classify(self):
        supplier_strategy = SupplierStrategy()
        tx = Transaction(self.book)
        tx.BeginEdit()

        tx.SetDescription("Postoextrasorocaba2686")
        self.assertEqual("Expenses:Auto:Gas", supplier_strategy.classify(tx))

        tx.SetDescription("Supplier Not Found!")
        self.assertIsNone(supplier_strategy.classify(tx))
        
