import os
import subprocess
import unittest

from io import StringIO


def specific_column(index, stdin, output):
    for line in stdin:
        output.write(line.split()[index - 1] + '\n')


def specific_column_with_cut(index, filepath):
    output = subprocess.check_output(
        'cut -f {} {}'.format(index, filepath), shell=True)
    return output.decode()


class TestCase(unittest.TestCase):

    def setUp(self):
        self.filepath = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            os.pardir,
            'data',
            'hightemp.txt')
        self.mock_stdin = open(self.filepath)
        self.mock_output = StringIO()

    def tearDown(self):
        self.mock_stdin.close()
        self.mock_output.close()

    def test_first_column(self):
        specific_column(1, self.mock_stdin, self.mock_output)
        actual = self.mock_output.getvalue()
        expected = specific_column_with_cut(1, self.filepath)
        self.assertEqual(actual, expected)

    def test_second_column(self):
        specific_column(2, self.mock_stdin, self.mock_output)
        actual = self.mock_output.getvalue()
        expected = specific_column_with_cut(2, self.filepath)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
