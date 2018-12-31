import csv

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
    # FIXME not working yet!
    def classify(split):
        classified_split = None
        account = None

        with open('classifier_rules.csv', 'r') as rules:
            reader = csv.reader(rules, delimiter=';')
            for row in reader:
                if row[0] == split.from:
                    account = row[1]

        if account == None:
           account =  "DEFAULT_ACCOUNT_GOES_HERE" # TODO get data in setup.cfg - or do not modify original split_to.GetAccount

        if not super.validate_split(account):
            raise Error("validate split failed!!!")

        classified_split.to = account

        return classified_split
