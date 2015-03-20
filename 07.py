# -*- coding: utf-8 -*-

def sentence(x, y, z):
    return u'{0}時の{1}は{2}'.format(x, y, z)

print(sentence(12, u'気温', 22.4))
