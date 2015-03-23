# -*- coding: utf-8 -*-

import os
import subprocess
import unittest

from mock import Mock

DATA_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'data')

def tail(filenames, n = 10):
    with open(filenames) as f:
        return ''.join(f.readlines()[-n:])

class TestCase(unittest.TestCase):

    def setUp(self):
        sys = Mock(argv=[__file__, 10])
        self.n = sys.argv[1]
        self.filename = os.path.join(DATA_DIR, 'hightemp.txt')

    def test(self):
        actual = tail(self.filename, self.n)
        expected = subprocess.check_output('tail {}'.format(self.filename), shell=True)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
