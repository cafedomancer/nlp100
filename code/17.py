import os
import subprocess
import unittest


def first_column_set(stdin):
    return ''.join(sorted(set(line.split()[0] + '\n' for line in stdin)))


def first_column_set_with_unix_commands(filepath):
    output = subprocess.check_output(
        'cut -f 1 {} | LC_ALL=C sort | uniq'.format(filepath), shell=True)
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

    def test_first_column_set(self):
        actual = first_column_set(self.mock_stdin)
        expected = first_column_set_with_unix_commands(self.filepath)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
