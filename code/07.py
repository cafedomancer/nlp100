# -*- coding: utf-8 -*-

import unittest

def formatted(x, y, z):
    return u'{}時の{}は{}'.format(x, y, z)

class TestCase(unittest.TestCase):

    def test(self):
        actual = formatted(12, u'気温', 22.4)
        expected = u'12時の気温は22.4'
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
