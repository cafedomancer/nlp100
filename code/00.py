import unittest


def reversed_string(string):
    return string[::-1]


class TestCase(unittest.TestCase):

    def test_reversed_string(self):
        actual = reversed_string('stressed')
        expected = 'desserts'
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
