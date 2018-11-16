import os
import logging
import datetime
from decimal import Decimal
from gnucash import Session, Transaction, Split, GncNumeric
from util import Util

class Ledger():
    # def __init__(self, curr, dry_run = True, src_file = Util().DEFAULT_GNUCASH_FILE):
    def __init__(self, currency, dry_run, src_file):
        self._currency = currency
        self._dry_run = dry_run
        self._src_file = src_file

    # def __init__(self, dry_run = True, src_file = Util().DEFAULT_GNUCASH_FILE):
    #     self._dry_run = dry_run
    #     self._src_file = src_file

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

    def write(self, account):
        session = Session(self.src_file)
        book = session.book
        currency = self.get_currency(book, self.currency)
        imported_items = set()

        for item in account.get_items(account, os.path.splitext(account.account_src_file)[1]):
            # TODO implement validation of imported items
            # if item.as_tuple() in imported_items:
            if item in imported_items:
                logging.info(Util.info("Skipped because it already was imported!!!"))
                continue

            self.create_tansaction(book, item, currency, account)
            # imported_items.add(item.as_tuple())
            imported_items.add(item)

        if self.dry_run:
            logging.info(Util.info('############### DRY-RUN ###############'))
        else:
            logging.info(Util.info('Saving GNUCash file..'))
            session.save()

        session.end()
        # session.destroy()       # TODO test it!

    def create_tansaction(self, book, item, curr, account):
        if curr is None:
            # FIXME default currency is hard-coded inside get_currency
            # curr = self.get_currency(book, Util().DEFAULT_CURRENCY)
            curr = self.get_currency(book, self.currency)

        if item is None:
            logging.error(Util.error("Could not create a gnucash transaction: missing item!!"))
            raise Exception("Could not create a gnucash transaction: missing item!!")

        if book is None:
            logging.error(Util.error("Could not create a gnucash transaction: missing book!!"))
            raise Exception("Could not create a gnucash transaction: missing book!!")

        acc_from = self.get_account(book, account.account_from)
        acc_to = self.get_account(book, account.to)
        # amount = int(Decimal(item.split_amount.replace(',', '.')) * curr.get_fraction()) # FIXME need it yet?
        amount = int(Decimal(item.amount) * curr.get_fraction())

        logging.debug(Util.debug("::::::::::::::::::::::::::::::::::::::::::::::::::::::::"))
        logging.debug(Util.debug("book...............: {b}".format(b = book)))
        logging.debug(Util.debug("account_name_from..: {a}".format(a = account.account_from)))
        logging.debug(Util.debug("name acc_from......: {name}".format(name = acc_from.GetName())))
        logging.debug(Util.debug("account_name_to....: {a}".format(a = account.to)))
        logging.debug(Util.debug("name acc_to........: {name}".format(name = acc_to.GetName())))
        logging.debug(Util.debug("[create_gnucash_transaction] amount: {a} :: curr: {c}".format(a = amount, c = curr.get_printname())))

        tx = Transaction(book)

        tx.BeginEdit()
        tx.SetCurrency(curr)
        # tx.SetDateEnteredTS(datetime.datetime.now())
        tx.SetDateEnteredSecs(datetime.datetime.now())
        # tx.SetDatePostedTS(item.date)
        tx.SetDatePostedSecs(item.date)
        tx.SetDescription(item.memo)

        split_from = Split(book)
        split_from.SetParent(tx)
        split_from.SetAccount(acc_from)
        split_from.SetValue(GncNumeric(amount, curr.get_fraction()))
        split_from.SetAmount(GncNumeric(amount, curr.get_fraction()))

        split_to = Split(book)
        split_to.SetParent(tx)
        split_to.SetAccount(acc_to)
        split_to.SetValue(GncNumeric(amount, curr.get_fraction()))
        split_to.SetAmount(GncNumeric(amount, curr.get_fraction()))

        tx.CommitEdit()

    def get_account(self, book, acc_name):
        return self.get_account_by_path(book.get_root_account(), acc_name.split(':'))

    def get_account_by_path(self, root, path):
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
            acc = self.get_account_by_path(acc, path[1:])

        return acc

    def get_currency(self, book, curr = 'BRL'):
        commod_tab = book.get_table()
        # currency = commod_tab.lookup('ISO4217', curr)  # FIXME curr isn't working.
        currency = commod_tab.lookup('ISO4217', 'BRL') # works!!!

        # curr_local = Util().DEFAULT_CURRENCY
        # currency = commod_tab.lookup('ISO4217', curr_local)
        # curr_local2 = 'BRL'
        # currency = commod_tab.lookup('ISO4217', curr_local2)
        # logging.debug(Util.debug('commod_tab: type => {c}, value => {v}'.format(c = type(commod_tab), v = commod_tab)))
        # logging.debug(Util.debug('currency: type => {curr_type}, value => {value}'.format(curr_type = type(currency), value = currency)))

        return currency
