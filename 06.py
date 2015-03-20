import re

def n_gram(sequence, n = 2, unit = 'word'):
    if unit == 'word':
        if isinstance(sequence, str):
            sequence = sequence.split()
        return [tuple(sequence[i:i + n]) for i in range(len(sequence) - n + 1)]
    elif unit == 'char':
        sequence = re.sub(r'\s', r'', sequence)
        if isinstance(sequence, str):
            sequence = list(sequence)
        return [tuple(sequence[i:i + n]) for i in range(len(sequence) - n + 1)]
    else:
        return None

sentence1 = 'paraparaparadise'
sentence2 = 'paragraph'

x = set(n_gram(sentence1, unit = 'char'))
y = set(n_gram(sentence2, unit = 'char'))

print(x | y)
print(x & y)
print(x - y)

target = tuple('se')

print(target in x)
print(target in y)
