import re
import unittest


def number_of_characters_of_each_word(string):
    return list(map(len, filter(None, re.split('\W+', string))))


class TestCase(unittest.TestCase):

    def test_number_of_characters_of_each_word(self):
        actual = number_of_characters_of_each_word(
                ('Now I need a drink, alcoholic of course, '
                 'after the heavy lectures involving quantum mechanics.'))
        expected = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
