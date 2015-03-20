# -*- coding: utf-8 -*-

import re
import unittest

def pi(string):
    string = re.sub(r'[^\w ]', r'', string)
    return [len(t) for t in string.split()]

class TestCase(unittest.TestCase):

    def test(self):
        actual = pi('Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.')
        expected = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
