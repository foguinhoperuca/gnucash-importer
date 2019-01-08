import csv
import logging
from util import Util

class Classifier:
    _strategy = None
    _AVAILABLE_STRATEGIES = {
        "SupplierStrategy",
        "TODO_IMPLEMENT"
    }

    def __init__(self, strategy):
        if strategy is None:
            raise ValueError("strategy can't be None! Please, inform the strategy that should be utilized to classify a transaction!")

        if not self.validate_strategy(strategy):
            raise ValueError("strategy must be valid! Please, inform a valid strategy from ({s}) that should be utilized to classify a transaction!".format(s = self.AVAILABLE_STRATEGIES))

        self._strategy = strategy

    @property
    def AVAILABLE_STRATEGIES(self):
        return self._AVAILABLE_STRATEGIES

    @property
    def strategy(self):
        return self._strategy
    @strategy.setter
    def strategy(self, value):
        self._strategy = value
    @strategy.deleter
    def strategy(self):
        del self._strategy
    
    def validate_strategy(self, strategy = _strategy):
        valid = False
        if strategy in self.AVAILABLE_STRATEGIES:
            valid = True

        return valid

    # TODO can be a method from account class?! Or be a different class to use composition?!
    def classify_account(self, account, description, strategy = None):
        classified_account = None
        classifier = None

        # FIXME optional parameter self.strategy (or even self._strategy) do not work!!!!
        if strategy is None:
            strategy = self.strategy

        if strategy == "SupplierStrategy":
            classifier = SupplierStrategy()

        logging.debug(Util.debug(classifier))
        classified_account = classifier.classify(description)

        if classified_account is None:
            classified_account = account

        logging.debug(Util.debug("classified_account --> {a}".format(a = classified_account)))
        return classified_account

# TODO implement as abstract class
class Strategy(object):
    def validate_split(split):
        print("TODO implement it!")
        return True

class SupplierStrategy(Strategy):
    def classify(self, description):
        account = None

        filename = Util.get_app_file('classifier_rules.csv')
        logging.debug(Util.debug("filename is..: {f}").format(f = filename))

        with open(filename, 'r', encoding='utf-8') as rules:
            reader = csv.reader(rules, delimiter=';')
            for row in reader:
                if row[0] == description:
                    account = row[1]
                    break

        logging.debug(Util.debug("account is: {a}".format(a = account)))

        return account
