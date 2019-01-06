import csv
import logging
from util import Util
from ledger import Ledger

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
    def classify_split(split, strategy = _strategy):
        classified_split = None

        if strategy == "SupplierStrategy":
            classified_split = SupplierStrategy.classify(split)

        return classified_split

# TODO implement as abstract class
class Strategy(object):
    def validate_split(split):
        print("TODO implement it!")
        return True

class SupplierStrategy(Strategy):
    def classify(self, transaction):
        account = None

        # TODO open classifier_rules.csv in correct path...
        with open('classifier_rules.csv', 'r') as rules:
            reader = csv.reader(rules, delimiter=';')
            for row in reader:
                if row[0] == transaction.GetDescription(): # FIXME validate rules against transaction.description!
                    account = row[1]
                    break

        logging.debug(Util.debug("account is: {a}".format(a = account)))

        return account
