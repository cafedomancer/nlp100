# -*- coding: utf-8 -*-

import os
import subprocess
import unittest

def lines(filename):
    with open(filename) as f:
        return len(f.readlines())

class TestCase(unittest.TestCase):

    def test(self):
        actual = lines(os.path.join('..', 'data', 'hightemp.txt'))
        expected = int(subprocess.check_output(['wc', '-l', os.path.join('..', 'data', 'hightemp.txt')]).split()[0])
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
