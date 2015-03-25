import os
import subprocess
import unittest

from itertools import islice


def last_lines(stdin, n=10):
    nlines = sum(1 for _ in stdin)
    stdin.seek(0)
    return ''.join(islice(stdin, nlines - n, nlines))


def last_lines_with_tail(filepath, n=10):
    output = subprocess.check_output(
        'tail -n {} {}'.format(n, filepath), shell=True)
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

    def test_last_lines(self):
        actual = last_lines(self.mock_stdin, self.mock_argv[1])
        expected = last_lines_with_tail(self.filepath, self.mock_argv[1])
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
