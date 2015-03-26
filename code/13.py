import os
import subprocess
import unittest


def merge_files(first, second):
    return ''.join(f.rstrip('\n') + '\t' + s
                   for f, s in zip(first, second))


def merge_files_with_paste(first, second):
    output = subprocess.check_output(
        'paste {} {}'.format(first, second), shell=True)
    return output.decode()


class TestCase(unittest.TestCase):

    def setUp(self):
        datadir = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            os.pardir,
            'data')
        self.col1_path = os.path.join(datadir, 'col1.txt')
        self.col2_path = os.path.join(datadir, 'col2.txt')
        self.col1 = open(self.col1_path)
        self.col2 = open(self.col2_path)

    def tearDown(self):
        self.col1.close()
        self.col2.close()

    def test_merge_files(self):
        actual = merge_files(self.col1, self.col2)
        expected = merge_files_with_paste(self.col1_path, self.col2_path)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
