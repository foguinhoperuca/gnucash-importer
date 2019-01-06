import unittest
from pathlib import Path
import gnucash_importer
from gnucash_importer.util import Util

class UtilTestCase(unittest.TestCase):
    def setUp(self):
        self.util = Util()

    def test_get_app_file(self):
        with self.assertRaises(ValueError) as context:
            self.util.get_app_file(None)
        self.assertTrue("Couldn't find None file in any path!", context.exception)

        with self.assertRaises(Exception) as context:
            self.util.get_app_file('app_file_not_found.cfg')
        self.assertTrue("Couldn't find app_file_not_found.cfg file in any path!", context.exception)

        self.assertEqual(Path('/etc/gnucash-magical-importer/setup.cfg'), self.util.get_app_file('setup.cfg'))
        self.assertEqual(Path("/etc/gnucash-magical-importer/classifier_rules.csv"), self.util.get_app_file('classifier_rules.csv'))
