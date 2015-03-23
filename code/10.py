# -*- coding: utf-8 -*-

import os
import subprocess
import unittest

def lines(filename):
    with open(filename) as f:
        return len(f.readlines())

class TestCase(unittest.TestCase):

    def test(self):
        filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'data', 'hightemp.txt')
        actual = lines(filename)
        expected = int(subprocess.check_output(['wc', '-l', filename]).split()[0])
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
