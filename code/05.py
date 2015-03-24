import unittest


def ngram(sequence, n):
    return zip(*(sequence[i:] for i in range(n)))


class TestCase(unittest.TestCase):

    def setUp(self):
        self.sentence = 'I am an NLPer'

    def test_word_bigram(self):
        actual = ngram(self.sentence.split(), 2)
        expected = [('I', 'am'), ('am', 'an'), ('an', 'NLPer')]
        self.assertEqual(actual, expected)

    def test_character_bigram(self):
        actual = ngram(self.sentence, 2)
        expected = [('I', ' '), (' ', 'a'), ('a', 'm'), ('m', ' '),
                    (' ', 'a'), ('a', 'n'), ('n', ' '), (' ', 'N'),
                    ('N', 'L'), ('L', 'P'), ('P', 'e'), ('e', 'r')]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
