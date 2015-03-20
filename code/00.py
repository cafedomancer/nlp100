# -*- coding: utf-8 -*-

import unittest

def reversed(string):
    return string[::-1]

class TestCase(unittest.TestCase):

    def test(self):
        actual = reversed('stressed')
        expected = 'desserts'
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
