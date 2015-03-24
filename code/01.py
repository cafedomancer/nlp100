import unittest


def odd_numbered_characters(string):
    return string[::2]


class TestCase(unittest.TestCase):

    def test_odd_numbered_characters(self):
        actual = odd_numbered_characters('パタトクカシーー')
        expected = 'パトカー'
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
