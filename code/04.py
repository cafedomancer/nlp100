import re
import unittest


def sliced_string(index, word):
    indices = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    return word[:1] if index in indices else word[:2]


def chemical_symbols(string):
    words = filter(None, re.split('\W+', string))
    return {sliced_string(i, w): i for i, w in enumerate(words, start=1)}


class TestCase(unittest.TestCase):

    def test_chemical_symbols(self):
        actual = chemical_symbols((
            'Hi He Lied Because Boron Could Not Oxidize Fluorine. '
            'New Nations Might Also Sign Peace Security Clause. '
            'Arthur King Can.'))
        expected = {'H': 1, 'He': 2, 'Li': 3, 'Be': 4, 'B': 5,
                    'C': 6, 'N': 7, 'O': 8, 'F': 9, 'Ne': 10,
                    'Na': 11, 'Mi': 12, 'Al': 13, 'Si': 14, 'P': 15,
                    'S': 16, 'Cl': 17, 'Ar': 18, 'K': 19, 'Ca': 20}
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
