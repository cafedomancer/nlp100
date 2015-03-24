import random
import unittest


def middle_shuffled_string(string):
    head = string[0]
    middle = string[1:-1]
    last = string[-1]

    chars = list(middle)
    random.shuffle(chars)
    middle = ''.join(chars)

    return ''.join(head + middle + last)


def typoglycemia(string):
    return ' '.join(middle_shuffled_string(w) if len(w) > 4 else w
                    for w in string.split())


class TestCase(unittest.TestCase):

    def test_typoglycemia(self):
        actual = typoglycemia((
            "I couldn't believe that I could actually understand what "
            "I was reading : the phenomenal power of the human mind ."))
        expected = ("I c[ouldn']{6}t b[eliev]{5}e that I c[oul]{3}d "
                    "a[ctuall]{6}y u[nderstan]{8}d what I was r[eadin]{5}g : "
                    "the p[henomena]{8}l p[owe]{3}r of the h[uma]{3}n mind .")
        self.assertRegex(actual, expected)


if __name__ == '__main__':
    unittest.main()
