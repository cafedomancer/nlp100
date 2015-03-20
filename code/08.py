# -*- coding: utf-8 -*-

import re
import unittest

def cipher(string):
    def shift(matchobj):
        return chr(219 - ord(matchobj.group(0)))
    return re.sub(r'[a-z]', shift, string)

class TestCase(unittest.TestCase):

    def setUp(self):
        self.string = 'I am an NLPer'

    def test_cipher_with_encryption(self):
        actual = cipher(self.string)
        expected = 'I zn zm NLPvi'
        self.assertEqual(actual, expected)

    def test_cipher_with_decryption(self):
        actual = cipher(cipher(self.string))
        expected = self.string
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
