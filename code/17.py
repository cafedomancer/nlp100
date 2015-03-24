# -*- coding: utf-8 -*-

import os
import subprocess
import unittest

DATA_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'data')

def first_column_difference(filename):
    with open(filename) as f:
        first = [r.split()[0] for r in f.readlines()]
    return '\n'.join(sorted(set(first))) + '\n'

class TestCase(unittest.TestCase):

    def setUp(self):
        self.filename = os.path.join(DATA_DIR, 'hightemp.txt')

    def test(self):
        actual = first_column_difference(self.filename)
        expected = subprocess.check_output('cut -f 1 {} | LC_ALL=C sort | uniq'.format(self.filename), shell=True)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
