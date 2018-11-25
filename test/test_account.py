import logging
import unittest
import gnucash_importer

from gnucash_importer.account import Nubank

class AccountTestCase(unittest.TestCase):
    def test_get_items(self):
        account = Nubank('example/local/nubank-2016-10.ofx') # FIXME need use a public fixture

        self.assertEqual(len(account.get_items()), 9)
