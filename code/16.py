# -*- coding: utf-8 -*-

import os
import subprocess
import unittest

from mock import Mock

DATA_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'data')

def split(filenames, n = 10):
    with open(filenames) as f:
        lines = f.readlines()
    return [''.join(lines[i:i + n]) for i in range(0, len(lines), n)]

class TestCase(unittest.TestCase):

    def setUp(self):
        sys = Mock(argv=[__file__, 10])
        self.n = sys.argv[1]
        self.filename = os.path.join(DATA_DIR, 'hightemp.txt')

    def test(self):
        actual = split(self.filename, self.n)
        subprocess.check_call('split -l 10 {}'.format(self.filename), shell=True)
        with open('xaa') as a, open('xab') as b, open('xac') as c:
            expected = [a.read(), b.read(), c.read()]
        self.assertEqual(actual, expected)

    def tearDown(self):
        subprocess.check_call('rm xaa', shell=True)
        subprocess.check_call('rm xab', shell=True)
        subprocess.check_call('rm xac', shell=True)

if __name__ == '__main__':
    unittest.main()
