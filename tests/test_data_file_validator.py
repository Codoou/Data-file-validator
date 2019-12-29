import unittest

import data_file_validator


class Data_file_validatorTestCase(unittest.TestCase):

    def setUp(self):
        self.app = data_file_validator.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        self.assertIn('Welcome to data-file-validator', rv.data.decode())


if __name__ == '__main__':
    unittest.main()
