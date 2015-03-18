# -*- coding: utf-8 -*-

zipped = zip(u'パトカー', u'タクシー')
print(''.join(map(lambda (x, y): x + y, zipped)))
