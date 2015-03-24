import re
import unittest


def chemical_symbols(string):
    string = re.sub(r'[^\w ]', r'', string)
    indices = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    return {t[:1] if i + 1 in indices else t[:2]: i + 1 for i, t in enumerate(string.split())}


class TestCase(unittest.TestCase):

    def test(self):
        actual = chemical_symbols(
            'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.')
        expected = {'H': 1, 'He': 2, 'Li': 3, 'Be': 4, 'B': 5, 'C': 6, 'N': 7, 'O': 8, 'F': 9, 'Ne': 10,
                    'Na': 11, 'Mi': 12, 'Al': 13, 'Si': 14, 'P': 15, 'S': 16, 'Cl': 17, 'Ar': 18, 'K': 19, 'Ca': 20}
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
