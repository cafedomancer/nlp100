import gzip
import json
import os
import unittest


def united_kingdom(filepath):
    with gzip.open(filepath, 'rt') as data:
        for datum in data:
            article = json.loads(datum)
            if article['title'] == 'イギリス':
                return article['text']


class TestCase(unittest.TestCase):

    def setUp(self):
        self.filepath = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            os.pardir,
            'data',
            'jawiki-country.json.gz')

    def test_united_kingdom(self):
        self.assertTrue(
            united_kingdom(self.filepath).startswith('{{redirect|UK}}'))


if __name__ == '__main__':
    unittest.main()
