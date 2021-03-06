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


def media_files(text):
    return re.findall(('(?:\[\[)?(?:File|ファイル):'
                       '(.+?(?:png|gif|jpg|jpeg|xcf|pdf|mid|ogg|svg|djvu))'
                       '.*?(?:\]\])?'),
                      text,
                      re.IGNORECASE)


class TestCase(unittest.TestCase):

    def setUp(self):
        self.filepath = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            os.pardir,
            'data',
            'jawiki-country.json.gz')
        self.text = united_kingdom(self.filepath)

    def test_media_files(self):
        actual = media_files(self.text)
        expected = ['Royal Coat of Arms of the United Kingdom.svg',
                    'Battle of Waterloo 1815.PNG',
                    'The British Empire.png',
                    'Uk topo en.jpg',
                    'BenNevis2005.jpg',
                    ('Elizabeth II greets NASA GSFC employees, '
                     'May 8, 2007 edit.jpg'),
                    'Palace of Westminster, London - Feb 2007.jpg',
                    ('David Cameron and Barack Obama '
                     'at the G20 Summit in Toronto.jpg'),
                    'Soldiers Trooping the Colour, 16th June 2007.jpg',
                    'Scotland Parliament Holyrood.jpg',
                    'London.bankofengland.arp.jpg',
                    ('City of London skyline from London City Hall '
                     '- Oct 2008.jpg'),
                    'Oil platform in the North SeaPros.jpg',
                    'Eurostar at St Pancras Jan 2008.jpg',
                    'Heathrow T5.jpg',
                    'Anglospeak.svg',
                    'CHANDOS3.jpg',
                    'The Fabs.JPG',
                    'PalaceOfWestminsterAtNight.jpg',
                    'Westminster Abbey - West Door.jpg',
                    'Edinburgh Cockburn St dsc06789.jpg',
                    'Canterbury Cathedral - Portal Nave Cross-spire.jpeg',
                    'Kew Gardens Palm House, London - July 2009.jpg',
                    ('2005-06-27 - United Kingdom '
                     '- England - London - Greenwich.jpg'),
                    'Stonehenge2007 07 30.jpg',
                    'Yard2.jpg',
                    'Durham Kathedrale Nahaufnahme.jpg',
                    'Roman Baths in Bath Spa, England - July 2006.jpg',
                    'Fountains Abbey view02 2005-08-27.jpg',
                    'Blenheim Palace IMG 3673.JPG',
                    'Liverpool Pier Head by night.jpg',
                    'Hadrian\'s Wall view near Greenhead.jpg',
                    'London Tower (1).JPG',
                    'Wembley Stadium, illuminated.jpg']
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
