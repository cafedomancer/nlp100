# -*- coding: utf-8 -*-

import unittest

def ngram(sequence, n, unit):
    if isinstance(sequence, str):
        if unit == 'word':
            sequence = sequence.split()
        elif unit == 'character':
            sequence = list(sequence)
    return zip(*(sequence[i:] for i in range(n)))

def union(x, y):
    return x | y

def intersection(x, y):
    return x & y

def difference(x, y):
    return x - y

def included(x, s):
    return x in s

class TestCase(unittest.TestCase):

    def setUp(self):
        self.x = set(ngram('paraparaparadise', 2, 'character'))
        self.y = set(ngram('paragraph', 2, 'character'))

    def test_union(self):
        actual = union(self.x, self.y)
        expected = {('p', 'a'), ('a', 'r'), ('r', 'a'), ('a', 'p'), ('a', 'd'), ('d', 'i'), ('i', 's'), ('s', 'e'), ('a', 'g'), ('g', 'r'), ('p', 'h')}
        self.assertEqual(actual, expected)

    def test_intersection(self):
        actual = intersection(self.x, self.y)
        expected = {('p', 'a'), ('a', 'r'), ('r', 'a'), ('a', 'p')}
        self.assertEqual(actual, expected)

    def test_difference(self):
        actual = difference(self.x, self.y)
        expected = {('a', 'd'), ('d', 'i'), ('i', 's'), ('s', 'e')}
        self.assertEqual(actual, expected)

    def test_included_in_x(self):
        actual = included(tuple('se'), self.x)
        expected = True
        self.assertEqual(actual, expected)

    def test_included_in_y(self):
        actual = included(tuple('se'), self.y)
        expected = False 
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
