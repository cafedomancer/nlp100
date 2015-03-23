# -*- coding: utf-8 -*-

import os
import subprocess
import unittest

DATA_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'data')

def separate_field(filename):
    with open(filename) as f:
        cols = [line.split()[:2] for line in f.readlines()]
    with open(os.path.join(DATA_DIR, 'col1.txt'), 'w') as f:
        f.write('\n'.join([r[0] for r in cols]))
        f.write('\n')
    with open(os.path.join(DATA_DIR, 'col2.txt'), 'w') as f:
        f.write('\n'.join([r[1] for r in cols]))
        f.write('\n')

class TestCase(unittest.TestCase):

    def setUp(self):
        self.filename = os.path.join(DATA_DIR, 'hightemp.txt')

    def test(self):
        separate_field(self.filename)

        with open(os.path.join(DATA_DIR, 'col1.txt')) as f:
            actual = f.read()
        expected = subprocess.check_output('cut -f 1 {}'.format(self.filename), shell=True)
        self.assertEqual(actual, expected)

        with open(os.path.join(DATA_DIR, 'col2.txt')) as f:
            actual = f.read()
        expected = subprocess.check_output('cut -f 2 {}'.format(self.filename), shell=True)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
