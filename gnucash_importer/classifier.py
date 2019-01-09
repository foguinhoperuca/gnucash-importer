import csv
import logging
from util import Util

# TODO implement as abstract class
class Strategy(object):
    _name = None
    @property
    def name(self):
        return self._name

    # TODO test raise Exception
    def __init__(self):
        raise Exception("Can't instantiate this class because it intented to be an abstract class.")

class SupplierStrategy(Strategy):
    def __init__(self):
        self._name = "Supplier Strategy"

    def classify(self, description):
        account = None

        with open(Util.get_app_file('classifier_rules.csv'), 'r', encoding='utf-8') as rules:
            reader = csv.reader(rules, delimiter=';')
            for row in reader:
                if row[0] == description:
                    account = row[1]
                    break

        logging.debug(Util.debug("account is --> {a}".format(a = account)))

        return account

class Classifier:
    _strategy = None
    _AVAILABLE_STRATEGIES = {
        'SupplierStrategy': SupplierStrategy()
    }

    def __init__(self, strategy):
        if strategy is None:
            raise ValueError("strategy can't be None! Please, inform the strategy that should be utilized to classify a transaction!")

        if not self.is_valid_strategy(strategy):
            raise ValueError("strategy must be valid! Please, inform a valid strategy from ({s}) that should be utilized to classify a transaction!".format(s = self.AVAILABLE_STRATEGIES))

        self._strategy = self.AVAILABLE_STRATEGIES[strategy]

    @property
    def AVAILABLE_STRATEGIES(self):
        return self._AVAILABLE_STRATEGIES

    @property
    def strategy(self):
        return self._strategy
    # # FIXME could be dangerous remove or update the setted strategy?!?!
    # @strategy.setter
    # def strategy(self, value):
    #     self._strategy = value
    # @strategy.deleter
    # def strategy(self):
    #     del self._strategy

    # TODO use @staticmethod or @classmethod here?!?
    @classmethod
    def is_valid_strategy(cls, strategy):
        # return strategy in self.AVAILABLE_STRATEGIES
        return strategy in cls._AVAILABLE_STRATEGIES

    # TODO can be a method from account class?! Or be a different class to use composition?!
    def classify_account(self, account, description):
        """A defined strategy is mandatory to this class. Therefore, this method don't need verify if a valid strategy was defined. This job is executed when the object is instantiate."""

        classified_account = self.strategy.classify(description)
        if classified_account is None:
            classified_account = account

        return classified_account
