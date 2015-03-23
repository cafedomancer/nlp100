# -*- coding: utf-8 -*-

import os
import subprocess
import unittest

def tab_to_space(filename):
    with open(filename) as f:
        return f.read().replace('\t', ' ')

class TestCase(unittest.TestCase):

    def setUp(self):
        self.filename = os.path.join('..', 'data', 'hightemp.txt')

    def test_tab_to_space_with_sed(self):
        actual = tab_to_space(self.filename)
        expected = subprocess.check_output('sed s/$\'\\t\'/\ /g {}'.format(self.filename), shell=True)
        self.assertEqual(actual, expected)

    def test_tab_to_space_with_tr(self):
        actual = tab_to_space(self.filename)
        expected = subprocess.check_output('tr "\t" " " < {}'.format(self.filename), shell=True)
        self.assertEqual(actual, expected)

    def test_tab_to_space_with_expand(self):
        actual = tab_to_space(self.filename)
        expected = subprocess.check_output('expand -t 1 {}'.format(self.filename), shell=True)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
