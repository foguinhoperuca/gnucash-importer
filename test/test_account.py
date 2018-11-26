import logging
import unittest
import gnucash_importer
from gnucash_importer.util import Util

from gnucash_importer.account import Nubank

class AccountTestCase(unittest.TestCase):
    def test_get_items(self):
        account = Nubank(Util().DEFAULT_ACCOUNT_SRC_FILE)

        self.assertEqual(len(account.get_items()), 9)
