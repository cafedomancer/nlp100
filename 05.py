import re

def n_gram(sequence, n = 2, unit = 'word'):
    if unit == 'word':
        if isinstance(sequence, str):
            sequence = sequence.split()
        return [sequence[i:i + n] for i in range(len(sequence) - n + 1)]
    elif unit == 'char':
        sequence = re.sub(r'\s', r'', sequence)
        if isinstance(sequence, str):
            sequence = list(sequence)
        return [sequence[i:i + n] for i in range(len(sequence) - n + 1)]
    else:
        return None

sentence = 'I am an NLPer'
print(n_gram(sentence, unit = 'word'))
print(n_gram(sentence, unit = 'char'))
