# -*- coding: utf-8 -*-

import os
import subprocess
import unittest

DATA_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'data')

def merge(first, second):
    with open(first) as f, open(second) as s:
        zipped = zip(f.read().splitlines(), s.read().splitlines())
    return '\n'.join('\t'.join(t) for t in zipped) + '\n'

class TestCase(unittest.TestCase):

    def setUp(self):
        self.filenames = (os.path.join(DATA_DIR, 'col1.txt'), os.path.join(DATA_DIR, 'col2.txt'))

    def test(self):
        actual = merge(*self.filenames)
        expected = subprocess.check_output('paste {} {}'.format(*self.filenames), shell=True)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
