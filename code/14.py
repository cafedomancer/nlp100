import os
import subprocess
import unittest

from itertools import islice


def first_lines(stdin, n=10):
    return ''.join(islice(stdin, n))


def first_lines_with_head(filepath, n=10):
    output = subprocess.check_output(
        'head -n {} {}'.format(n, filepath), shell=True)
    return output.decode()


class TestCase(unittest.TestCase):

    def setUp(self):
        self.filepath = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            os.pardir,
            'data',
            'hightemp.txt')
        self.mock_stdin = open(self.filepath)
        self.mock_argv = [__file__, 5]

    def tearDown(self):
        self.mock_stdin.close()

    def test_first_lines(self):
        actual = first_lines(self.mock_stdin, self.mock_argv[1])
        expected = first_lines_with_head(self.filepath, self.mock_argv[1])
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
