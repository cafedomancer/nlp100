import unittest


def zipped_string(first, second):
    return ''.join(sum(zip(first, second), ()))


class TestCase(unittest.TestCase):

    def test_zipped_string(self):
        actual = zipped_string('パトカー', 'タクシー')
        expected = 'パタトクカシーー'
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
