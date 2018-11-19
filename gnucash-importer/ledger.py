import logging
import datetime
from decimal import Decimal
from gnucash import Session, Transaction, Split, GncNumeric
from util import Util

"""
Meant to be the main interaction with GnuCash
"""
class Ledger():
    _account = None
    _currency = None
    _dry_run = None
    _src_file = None

    def __init__(self, account, currency = Util().DEFAULT_CURRENCY, dry_run = True, src_file = Util().DEFAULT_GNUCASH_FILE):
        self._account = account
        self._currency = currency
        self._dry_run = dry_run
        self._src_file = src_file

    @property
    def account(self):
        return self._account
    @account.setter
    def account(self, value):
        self._account = value
    @account.deleter
    def account(self):
        del self._account

    @property
    def currency(self):
        return self._currency
    @currency.setter
    def currency(self, value):
        self._currency = value
    @currency.deleter
    def currency(self):
        del self._currency

    @property
    def dry_run(self):
        return self._dry_run
    @dry_run.setter
    def dry_run(self, value):
        self._dry_run = value
    @dry_run.deleter
    def dry_run(self):
        del self._dry_run

    @property
    def src_file(self):
        return self._src_file
    @src_file.setter
    def src_file(self, value):
        self._src_file = value
    @src_file.deleter
    def src_file(self):
        del self._src_file

    def write(self):
        session = Session(self.src_file)
        gnucash_book = session.book
        imported_items = set()

        for item in self.account.get_items():
            # TODO implement validation of imported items
            if item in imported_items:
                logging.info(Util.info("Skipped because it already was imported!!!"))
                continue

            self.create_tansaction(gnucash_book, item)
            # imported_items.add(item.as_tuple())
            imported_items.add(item)

        if self.dry_run:
            logging.info(Util.info('############### DRY-RUN ###############'))
        else:
            logging.info(Util.info('Saving GNUCash file..'))
            session.save()

        session.end()
        # session.destroy()       # TODO test it!

    # TODO fill better - more splits...
    def create_tansaction(self, gnucash_book, item):
        if gnucash_book is None:
            logging.error(Util.error("Could not create a gnucash transaction: missing book!!"))
            raise Exception("Could not create a gnucash transaction: missing book!!")

        if item is None:
            logging.error(Util.error("Could not create a gnucash transaction: missing item!!"))
            raise Exception("Could not create a gnucash transaction: missing item!!")

        gnucash_currency = self.get_gnucash_currency(gnucash_book, self.currency)
        gnucash_acc_from = self.get_gnucash_account(gnucash_book, self.account.acc_from)
        gnucash_acc_to = self.get_gnucash_account(gnucash_book, self.account.acc_to)
        # amount = int(Decimal(item.split_amount.replace(',', '.')) * curr.get_fraction()) # FIXME need it yet?
        amount = int(Decimal(item.amount) * gnucash_currency.get_fraction())

        logging.debug(Util.debug("::::::::::::::::::::::::::::::::::::::::::::::::::::::::"))
        logging.debug(Util.debug("gnucash_currency..: {c}".format(c = gnucash_currency.get_printname())))
        logging.debug(Util.debug("book..............: {b}".format(b = gnucash_book)))
        logging.debug(Util.debug("name acc_from.....: {name}".format(name = gnucash_acc_from.GetName())))
        logging.debug(Util.debug("name acc_to.......: {name}".format(name = gnucash_acc_to.GetName())))
        logging.debug(Util.debug("amount............: {a}".format(a = amount)))

        tx = Transaction(gnucash_book)

        tx.BeginEdit()
        tx.SetCurrency(gnucash_currency)
        tx.SetDescription(item.memo)
        # tx.SetDateEnteredTS(datetime.datetime.now())
        tx.SetDateEnteredSecs(datetime.datetime.now())
        # tx.SetDatePostedTS(item.date)
        tx.SetDatePostedSecs(item.date)

        split_from = Split(gnucash_book)
        split_from.SetParent(tx)
        split_from.SetAccount(gnucash_acc_from)
        split_from.SetValue(GncNumeric(amount, gnucash_currency.get_fraction()))
        split_from.SetAmount(GncNumeric(amount, gnucash_currency.get_fraction()))

        split_to = Split(gnucash_book)
        split_to.SetParent(tx)
        split_to.SetAccount(gnucash_acc_to)
        split_to.SetValue(GncNumeric(amount, gnucash_currency.get_fraction()))
        split_to.SetAmount(GncNumeric(amount, gnucash_currency.get_fraction()))

        tx.CommitEdit()

    def get_gnucash_account(self, book, acc_name):
        return self.get_gnucash_account_by_path(book.get_root_account(), acc_name.split(':'))

    def get_gnucash_account_by_path(self, root, path):
        acc = None
        if not root == None:
            acc = root.lookup_by_name(path[0])
            logging.debug(Util.debug("root.....: {a}".format(a = root.GetName())))
            logging.debug(Util.debug("path[0]..: {p}".format(p = path[0])))
            logging.debug(Util.debug("acc......: {a}".format(a = acc.GetName())))

        if acc.get_instance() == None:
            raise Exception('NO Good: account path not found --> %s' % (path[0]))

        logging.debug(Util.debug("path: {path} len(path): {lenght} name: {name}".format(path = path, lenght = len(path), name = acc.GetName())))

        if len(path) > 1:
            acc = self.get_gnucash_account_by_path(acc, path[1:])

        return acc

    def get_gnucash_currency(self, book, curr = 'BRL'):
        commod_tab = book.get_table()
        # currency = commod_tab.lookup('ISO4217', curr)  # FIXME curr isn't working.
        gnucash_currency = commod_tab.lookup('ISO4217', 'BRL') # works!!!

        # curr_local = Util().DEFAULT_CURRENCY
        # gnucash_currency = commod_tab.lookup('ISO4217', curr_local)
        # curr_local2 = 'BRL'
        # gnucash_currency = commod_tab.lookup('ISO4217', curr_local2)
        # logging.debug(Util.debug('commod_tab: type => {c}, value => {v}'.format(c = type(commod_tab), v = commod_tab)))
        # logging.debug(Util.debug('currency: type => {curr_type}, value => {value}'.format(curr_type = type(gnucash_currency), value = gnucash_currency)))

        return gnucash_currency
