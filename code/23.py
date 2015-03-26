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


def section_names_and_levels(text):
    return [(name, len(level))
            for name, level in re.findall('={2,4}(.+?)(={2,4})', text)]


class TestCase(unittest.TestCase):

    def setUp(self):
        self.filepath = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            os.pardir,
            'data',
            'jawiki-country.json.gz')
        self.text = united_kingdom(self.filepath)

    def test_section_names_and_levels(self):
        actual = section_names_and_levels(self.text)
        expected = [('国名', 2), ('歴史', 2), ('地理', 2), ('気候', 3),
                    ('政治', 2), ('外交と軍事', 2), ('地方行政区分', 2),
                    ('主要都市', 3), ('科学技術', 2), ('経済', 2),
                    ('鉱業', 3), ('農業', 3), ('貿易', 3), ('通貨', 3),
                    ('企業', 3), ('交通', 2), ('道路', 3), ('鉄道', 3),
                    ('海運', 3), ('航空', 3), ('通信', 2), ('国民', 2),
                    ('言語', 3), ('宗教', 3), (' 婚姻 ', 3), ('教育', 3),
                    ('文化', 2), ('食文化', 3), ('文学', 3), (' 哲学 ', 3),
                    ('音楽', 3), ('イギリスのポピュラー音楽', 4),
                    ('映画', 3), ('コメディ', 3), ('国花', 3),
                    ('世界遺産', 3), ('祝祭日', 3), ('スポーツ', 2),
                    ('サッカー', 3), ('競馬', 3), ('モータースポーツ', 3),
                    ('脚注', 2), ('関連項目', 2), ('外部リンク', 2)]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
