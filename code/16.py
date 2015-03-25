import glob
import math
import os
import subprocess
import unittest

from itertools import islice


def split_file(stdin, n):
    nlines = sum(1 for _ in stdin)
    l = math.ceil(nlines / n)
    result = []
    for i in range(0, nlines, l):
        stdin.seek(0)
        result.append(''.join(islice(stdin, i, i + l)))
    return result


def split_file_with_split(filepath, n):
    output = subprocess.check_output('wc {}'.format(filepath), shell=True)
    nlines = int(output.split()[0])
    l = math.ceil(nlines / n)
    subprocess.check_call('split -l {} {}'.format(l, filepath), shell=True)


def splitted_files():
    result = []
    for name in glob.glob('x[a-z][a-z]'):
        with open(name) as f:
            result.append(f.read())
    return result


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
        subprocess.check_call('rm -f x[a-z][a-z]', shell=True)

    def test_split_file(self):
        actual = split_file(self.mock_stdin, self.mock_argv[1])
        split_file_with_split(self.filepath, self.mock_argv[1])
        expected = splitted_files()
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
