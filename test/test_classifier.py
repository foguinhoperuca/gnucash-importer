import logging
import unittest
import gnucash_importer
from gnucash_importer.util import Util
from gnucash_importer.classifier import Classifier, Strategy, SupplierStrategy
from gnucash_importer.account import Account, Nubank
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

    # @unittest.skip("TODO implement it!")
    def test_classify_account(self):
        nubank = Nubank(Util().DEFAULT_ACCOUNT_SRC_FILE)
        classifier = Classifier("SupplierStrategy")
        items = nubank.get_items()

        gnucash_acc_to = classifier.classify_account(nubank.acc_to, items[0].memo)
        self.assertEqual(self.util.DEFAULT_NUBANK_TO, gnucash_acc_to)

        gnucash_acc_to = classifier.classify_account(nubank.acc_to, items[1].memo)
        self.assertEqual("Expenses:Groceries", gnucash_acc_to)

        gnucash_acc_to = classifier.classify_account(nubank.acc_to, items[2].memo)
        self.assertEqual("Expenses:Pets", gnucash_acc_to)

        gnucash_acc_to = classifier.classify_account(nubank.acc_to, items[3].memo)
        self.assertEqual("Expenses:Transport:Auto:Gas", gnucash_acc_to)

        gnucash_acc_to = classifier.classify_account(nubank.acc_to, items[4].memo)
        self.assertEqual(self.util.DEFAULT_NUBANK_TO, gnucash_acc_to)

        gnucash_acc_to = classifier.classify_account(nubank.acc_to, items[5].memo)
        self.assertEqual(self.util.DEFAULT_NUBANK_TO, gnucash_acc_to)

        gnucash_acc_to = classifier.classify_account(nubank.acc_to, items[6].memo)
        self.assertEqual(self.util.DEFAULT_NUBANK_TO, gnucash_acc_to)

        gnucash_acc_to = classifier.classify_account(nubank.acc_to, items[7].memo)
        self.assertEqual(self.util.DEFAULT_NUBANK_TO, gnucash_acc_to)

        gnucash_acc_to = classifier.classify_account(nubank.acc_to, items[8].memo)
        self.assertEqual("Expenses:Transport:Auto:Gas", gnucash_acc_to)




    @unittest.skip("TODO implement it!")
    def test_validate_split(self):
        pass

    def test_classify(self):
        supplier_strategy = SupplierStrategy()

        found = "Postoextrasorocaba2686"
        self.assertEqual("Expenses:Transport:Auto:Gas", supplier_strategy.classify(found))

        not_found = "Supplier Not Found!"
        self.assertIsNone(supplier_strategy.classify(not_found))
        
