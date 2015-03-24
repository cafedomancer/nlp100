import re
import unittest


def lengths_of_each_word(string):
    return list(map(len, filter(None, re.split('\W+', string))))


class TestCase(unittest.TestCase):

    def test_lengths_of_each_word(self):
        actual = lengths_of_each_word(
                ('Now I need a drink, alcoholic of course, '
                 'after the heavy lectures involving quantum mechanics.'))
        expected = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
