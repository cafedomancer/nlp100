# -*- coding: utf-8 -*-

import unittest

def odd(string):
    return string[::2]

class TestCase(unittest.TestCase):

    def test(self):
        actual = odd(u'パタトクカシーー')
        expected = u'パトカー'
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
