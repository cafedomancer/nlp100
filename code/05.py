# -*- coding: utf-8 -*-

import unittest

def ngram(sequence, n, unit):
    if isinstance(sequence, str):
        if unit == 'word':
            sequence = sequence.split()
        elif unit == 'character':
            sequence = list(sequence)
    return zip(*(sequence[i:] for i in range(n)))

class TestCase(unittest.TestCase):

    def setUp(self):
        self.sentence = 'I am an NLPer'

    def test_word_bigram_with_string(self):
        actual = ngram(self.sentence, 2, 'word')
        expected = [('I', 'am'), ('am', 'an'), ('an', 'NLPer')]
        self.assertEqual(actual, expected)

    def test_word_bigram_with_list(self):
        actual = ngram(self.sentence.split(), 2, 'word')
        expected = [('I', 'am'), ('am', 'an'), ('an', 'NLPer')]
        self.assertEqual(actual, expected)

    def test_character_bigram_with_string(self):
        actual = ngram(self.sentence, 2, 'character')
        expected = [('I', ' '), (' ', 'a'), ('a', 'm'), ('m', ' '), (' ', 'a'), ('a', 'n'), ('n', ' '), (' ', 'N'), ('N', 'L'), ('L', 'P'), ('P', 'e'), ('e', 'r')]
        self.assertEqual(actual, expected)

    def test_character_bigram_with_list(self):
        actual = ngram(list(self.sentence), 2, 'character')
        expected = [('I', ' '), (' ', 'a'), ('a', 'm'), ('m', ' '), (' ', 'a'), ('a', 'n'), ('n', ' '), (' ', 'N'), ('N', 'L'), ('L', 'P'), ('P', 'e'), ('e', 'r')]
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
