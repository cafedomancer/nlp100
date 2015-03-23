# -*- coding: utf-8 -*-

import unittest

def zipped(first, second):
    return ''.join(sum(zip(first, second), ()))

class TestCase(unittest.TestCase):

    def test(self):
        actual = zipped(u'パトカー', u'タクシー')
        expected = u'パタトクカシーー'
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
