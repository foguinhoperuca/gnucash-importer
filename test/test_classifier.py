import logging
import unittest
from termcolor import colored, cprint
import gnucash_importer
from gnucash_importer.util import Util
from gnucash_importer.classifier import Classifier, Strategy, SupplierStrategy, RegexStrategy
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
        self.assertEqual("Supplier Strategy", classifier.strategy.name)

        with self.assertRaises(ValueError) as context:
            Classifier(None)
            self.assertTrue("strategy can't be None! Please, inform the strategy that should be utilized to classify a transaction!", context.exception)

        with self.assertRaises(ValueError) as context:
            Classifier("NOT_AVAILABLE_STRATEGY")
            self.assertTrue("strategy must be valid! Please, inform a valid strategy from ({s}) that should be utilized to classify a transaction!".format(s = Classifier.AVAILABLE_STRATEGIES), context.exception)

    def test_is_valid_strategy(self):
        self.assertTrue(Classifier.is_valid_strategy("SupplierStrategy"))
        self.assertFalse(Classifier.is_valid_strategy("NotImplementedYet"))
        self.assertFalse(Classifier.is_valid_strategy(None))

    def test_classify_account(self):
        nubank = Nubank(Util().DEFAULT_ACCOUNT_SRC_FILE)
        items = nubank.get_items()

        classifier = Classifier("SupplierStrategy")
        gnucash_acc_to = classifier.classify_account(nubank.acc_to, items[0].memo)
        self.assertEqual(self.util.DEFAULT_NUBANK_TO, gnucash_acc_to)
        if logging.getLogger().getEffectiveLevel() == logging.DEBUG:
            logging.debug(colored("items[0].memo --> {m}".format(m = items[0].memo), 'yellow', attrs=['bold']))
            print(colored("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++", 'yellow', attrs=['bold']))
        gnucash_acc_to = classifier.classify_account(nubank.acc_to, items[1].memo)
        self.assertEqual("Expenses:Groceries", gnucash_acc_to)
        if logging.getLogger().getEffectiveLevel() == logging.DEBUG:
            logging.debug(colored("items[1].memo --> {m}".format(m = items[1].memo), 'yellow', attrs=['bold']))
            print(colored("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++", 'yellow', attrs=['bold']))
        gnucash_acc_to = classifier.classify_account(nubank.acc_to, items[2].memo)
        self.assertEqual("Expenses:Pets", gnucash_acc_to)
        if logging.getLogger().getEffectiveLevel() == logging.DEBUG:
            logging.debug(colored("items[2].memo --> {m}".format(m = items[2].memo), 'yellow', attrs=['bold']))
            print(colored("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++", 'yellow', attrs=['bold']))
        gnucash_acc_to = classifier.classify_account(nubank.acc_to, items[3].memo)
        self.assertEqual("Expenses:Transport:Auto:Gas", gnucash_acc_to)
        if logging.getLogger().getEffectiveLevel() == logging.DEBUG:
            logging.debug(colored("items[3].memo --> {m}".format(m = items[3].memo), 'yellow', attrs=['bold']))
            print(colored("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++", 'yellow', attrs=['bold']))
        gnucash_acc_to = classifier.classify_account(nubank.acc_to, items[4].memo)
        self.assertEqual(self.util.DEFAULT_NUBANK_TO, gnucash_acc_to)
        if logging.getLogger().getEffectiveLevel() == logging.DEBUG:
            logging.debug(colored("items[4].memo --> {m}".format(m = items[4].memo), 'yellow', attrs=['bold']))
            print(colored("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++", 'yellow', attrs=['bold']))
        gnucash_acc_to = classifier.classify_account(nubank.acc_to, items[5].memo)
        self.assertEqual(self.util.DEFAULT_NUBANK_TO, gnucash_acc_to)
        if logging.getLogger().getEffectiveLevel() == logging.DEBUG:
            logging.debug(colored("items[5].memo --> {m}".format(m = items[5].memo), 'yellow', attrs=['bold']))
            print(colored("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++", 'yellow', attrs=['bold']))
        gnucash_acc_to = classifier.classify_account(nubank.acc_to, items[6].memo)
        self.assertEqual(self.util.DEFAULT_NUBANK_TO, gnucash_acc_to)
        if logging.getLogger().getEffectiveLevel() == logging.DEBUG:
            logging.debug(colored("items[6].memo --> {m}".format(m = items[6].memo), 'yellow', attrs=['bold']))
            print(colored("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++", 'yellow', attrs=['bold']))
        gnucash_acc_to = classifier.classify_account(nubank.acc_to, items[7].memo)
        self.assertEqual(self.util.DEFAULT_NUBANK_TO, gnucash_acc_to)
        if logging.getLogger().getEffectiveLevel() == logging.DEBUG:
            logging.debug(colored("items[7].memo --> {m}".format(m = items[7].memo), 'yellow', attrs=['bold']))
            print(colored("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++", 'yellow', attrs=['bold']))
        gnucash_acc_to = classifier.classify_account(nubank.acc_to, items[8].memo)
        self.assertEqual("Expenses:Transport:Auto:Gas", gnucash_acc_to)
        if logging.getLogger().getEffectiveLevel() == logging.DEBUG:
            logging.debug(colored("items[8].memo --> {m}".format(m = items[8].memo), 'yellow', attrs=['bold']))
            print(colored("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++", 'yellow', attrs=['bold']))

        classifier = Classifier("RegexStrategy")
        gnucash_acc_to = classifier.classify_account(nubank.acc_to, items[0].memo)
        self.assertEqual("Expenses:Restaurant:Dining", gnucash_acc_to)
        if logging.getLogger().getEffectiveLevel() == logging.DEBUG:
            logging.debug(colored("items[0].memo --> {m}".format(m = items[0].memo), 'yellow', attrs=['bold']))
            print(colored("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++", 'yellow', attrs=['bold']))
        gnucash_acc_to = classifier.classify_account(nubank.acc_to, items[1].memo)
        self.assertEqual(self.util.DEFAULT_NUBANK_TO, gnucash_acc_to)
        if logging.getLogger().getEffectiveLevel() == logging.DEBUG:
            logging.debug(colored("items[1].memo --> {m}".format(m = items[1].memo), 'yellow', attrs=['bold']))
            print(colored("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++", 'yellow', attrs=['bold']))
        gnucash_acc_to = classifier.classify_account(nubank.acc_to, items[2].memo)
        self.assertEqual(self.util.DEFAULT_NUBANK_TO, gnucash_acc_to)
        if logging.getLogger().getEffectiveLevel() == logging.DEBUG:
            logging.debug(colored("items[2].memo --> {m}".format(m = items[2].memo), 'yellow', attrs=['bold']))
            print(colored("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++", 'yellow', attrs=['bold']))
        gnucash_acc_to = classifier.classify_account(nubank.acc_to, items[3].memo)
        self.assertEqual(self.util.DEFAULT_NUBANK_TO, gnucash_acc_to)
        if logging.getLogger().getEffectiveLevel() == logging.DEBUG:
            logging.debug(colored("items[3].memo --> {m}".format(m = items[3].memo), 'yellow', attrs=['bold']))
            print(colored("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++", 'yellow', attrs=['bold']))
        gnucash_acc_to = classifier.classify_account(nubank.acc_to, items[4].memo)
        self.assertEqual("Expenses:Groceries", gnucash_acc_to)
        if logging.getLogger().getEffectiveLevel() == logging.DEBUG:
            logging.debug(colored("items[4].memo --> {m}".format(m = items[4].memo), 'yellow', attrs=['bold']))
            print(colored("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++", 'yellow', attrs=['bold']))
        gnucash_acc_to = classifier.classify_account(nubank.acc_to, items[5].memo)
        self.assertEqual(self.util.DEFAULT_NUBANK_TO, gnucash_acc_to)
        if logging.getLogger().getEffectiveLevel() == logging.DEBUG:
            logging.debug(colored("items[5].memo --> {m}".format(m = items[5].memo), 'yellow', attrs=['bold']))
            print(colored("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++", 'yellow', attrs=['bold']))
        gnucash_acc_to = classifier.classify_account(nubank.acc_to, items[6].memo)
        self.assertEqual("Expenses:Taxes", gnucash_acc_to)
        if logging.getLogger().getEffectiveLevel() == logging.DEBUG:
            logging.debug(colored("items[6].memo --> {m}".format(m = items[6].memo), 'yellow', attrs=['bold']))
            print(colored("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++", 'yellow', attrs=['bold']))
        gnucash_acc_to = classifier.classify_account(nubank.acc_to, items[7].memo)
        self.assertEqual(self.util.DEFAULT_NUBANK_TO, gnucash_acc_to)
        if logging.getLogger().getEffectiveLevel() == logging.DEBUG:
            logging.debug(colored("items[7].memo --> {m}".format(m = items[7].memo), 'yellow', attrs=['bold']))
            print(colored("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++", 'yellow', attrs=['bold']))
        gnucash_acc_to = classifier.classify_account(nubank.acc_to, items[8].memo)
        self.assertEqual(self.util.DEFAULT_NUBANK_TO, gnucash_acc_to)
        if logging.getLogger().getEffectiveLevel() == logging.DEBUG:
            logging.debug(colored("items[8].memo --> {m}".format(m = items[8].memo), 'yellow', attrs=['bold']))
            print(colored("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++", 'yellow', attrs=['bold']))

    def test_classify(self):
        strategy = SupplierStrategy()
        found = "Postoextrasorocaba2686"
        self.assertEqual("Expenses:Transport:Auto:Gas", strategy.classify(found))
        not_found = "Supplier Not Found!"
        self.assertIsNone(strategy.classify(not_found))

        strategy = RegexStrategy()
        found = "CF 78339-32 Barbosa Supermercado LTDA"
        self.assertEqual("Expenses:Groceries", strategy.classify(found))
        found = "BK Wallmart Limao"
        self.assertEqual("Expenses:Restaurant:Dining", strategy.classify(found))
        found = "IOF de Google Play Cia"
        self.assertEqual("Expenses:Taxes", strategy.classify(found))
        not_found = "Regex Not Found!"
        self.assertIsNone(strategy.classify(not_found))
