# -*- coding: utf-8 -*-

import random
import unittest

def typoglycemia(string):
    def shuffled(token):
        head = token[0]
        middle = token[1:-1]
        last = token[-1]

        middle = list(middle)
        random.shuffle(middle)
        middle = ''.join(middle)

        return ''.join(head + middle + last)

    return ' '.join([shuffled(t) if len(t) > 4 else t for t in string.split()])

class TestCase(unittest.TestCase):

    def test(self):
        actual = typoglycemia("I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .")
        expected = r"I c[ouldn']{6}t b[eliev]{5}e that I c[oul]{3}d a[ctuall]{6}y u[nderstan]{8}d what I was r[eadin]{5}g : the p[henomena]{8}l p[owe]{3}r of the h[uma]{3}n mind ."
        self.assertRegexpMatches(actual, expected)

if __name__ == '__main__':
    unittest.main()
