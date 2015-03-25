import os
import subprocess
import unittest


def number_of_lines(stdin):
    return sum(1 for line in stdin)


def number_of_lines_with_wc(filepath):
    output = subprocess.check_output('wc {}'.format(filepath), shell=True)
    return int(output.split()[0])


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

    def test_number_of_lines(self):
        actual = number_of_lines(self.mock_stdin)
        expected = number_of_lines_with_wc(self.filepath)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
