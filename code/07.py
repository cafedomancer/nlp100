import unittest


def formatted_string(x, y, z):
    return '{}時の{}は{}'.format(x, y, z)


class TestCase(unittest.TestCase):

    def test_formatted_string(self):
        actual = formatted_string(12, '気温', 22.4)
        expected = '12時の気温は22.4'
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
