import os
import subprocess
import unittest


def tabs_to_spaces(stdin):
    return stdin.read().replace('\t', ' ')


def tabs_to_spaces_with_unix_command(command):
    output = subprocess.check_output(command, shell=True)
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

    def test_tabs_to_spaces_with_sed(self):
        actual = tabs_to_spaces(self.mock_stdin)
        expected = tabs_to_spaces_with_unix_command(
            "sed s/$'\\t'/\ /g {}".format(self.filepath))
        self.assertEqual(actual, expected)

    def test_tabs_to_spaces_with_tr(self):
        actual = tabs_to_spaces(self.mock_stdin)
        expected = tabs_to_spaces_with_unix_command(
            'tr "\t" " " < {}'.format(self.filepath))
        self.assertEqual(actual, expected)

    def test_tabs_to_spaces_with_expand(self):
        actual = tabs_to_spaces(self.mock_stdin)
        expected = tabs_to_spaces_with_unix_command(
            'expand -t 1 {}'.format(self.filepath))
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
