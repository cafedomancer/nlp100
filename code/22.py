import gzip
import json
import os
import re
import unittest


def united_kingdom(filepath):
    with gzip.open(filepath, 'rt') as data:
        for datum in data:
            article = json.loads(datum)
            if article['title'] == 'イギリス':
                return article['text']


def category_names(text):
    return re.findall('\[\[Category:(.+?)(?:\|.+?)?\]\]', text)


class TestCase(unittest.TestCase):

    def setUp(self):
        self.filepath = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            os.pardir,
            'data',
            'jawiki-country.json.gz')
        self.text = united_kingdom(self.filepath)

    def test_category_names(self):
        actual = category_names(self.text)
        expected = ['イギリス',
                    '英連邦王国',
                    'G8加盟国',
                    '欧州連合加盟国',
                    '海洋国家',
                    '君主国',
                    '島国',
                    '1801年に設立された州・地域']
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
