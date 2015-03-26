import os
import subprocess
import unittest

from collections import defaultdict


def sorted_word_frequency_of_first_column(stdin):
    firsts = [line.split()[0] for line in stdin]
    freq = defaultdict(int)
    for word in firsts:
        freq[word] += 1
    sorted_freq = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return ''.join('   {} {}\n'.format(f, w) for w, f in sorted_freq)


def sorted_word_frequency_of_first_column_with_unix_commands(filepath):
    output = subprocess.check_output(
        ('cut -f 1 {} | LC_ALL=C sort | '
         'uniq -c | LC_ALL=C sort -k 1 -n -r -s').format(filepath), shell=True)
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

    def test_sorted_word_frequency_of_first_column(self):
        actual = sorted_word_frequency_of_first_column(self.mock_stdin)
        expected = sorted_word_frequency_of_first_column_with_unix_commands(
            self.filepath)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
