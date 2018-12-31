import unittest
import gnucash_importer
from gnucash_importer.util import Util
from gnucash_importer.classifier import Classifier, Strategy, SupplierStrategy

class ClassifierTestCase(unittest.TestCase):
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
        # def classify(split)
