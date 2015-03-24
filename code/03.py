import re
import unittest


def each_word_length(string):
    return list(map(len, filter(None, re.split('\W+', string))))


class TestCase(unittest.TestCase):

    def test_each_word_length(self):
        actual = each_word_length((
            'Now I need a drink, alcoholic of course, '
            'after the heavy lectures involving quantum mechanics.'))
        print((
            'Now I need a drink, alcoholic of course, '
            'after the heavy lectures involving quantum mechanics.'))
        expected = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
