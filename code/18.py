import os
import subprocess
import unittest


def sorted_by_third_column(stdin):
    return ''.join(sorted(
        (line for line in stdin),
        key=lambda x: float(x.split()[2]),
        reverse=True))


def sorted_by_third_column_with_sort(filepath):
    output = subprocess.check_output(
            'LC_ALL=C sort -k 3 -n -r -s {}'.format(filepath), shell=True)
    return output.decode()


class TestCase(unittest.TestCase):

    def setUp(self):
        self.filepath = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            os.pardir,
            'data',
            'hightemp.txt')
        self.mock_stdin = open(self.filepath)

    def tearDown(self):
        self.mock_stdin.close()

    def test_sorted_by_third_column(self):
        actual = sorted_by_third_column(self.mock_stdin)
        expected = sorted_by_third_column_with_sort(self.filepath)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
