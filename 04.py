import re

sentences = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
sentences = re.sub(r'[,.]', '', sentences)

indices = [1, 5, 6, 7, 8, 9, 15, 16, 19]
indices = map(lambda x: x - 1, indices)

dictionary = {}
for i, word in enumerate(sentences.split()):
    if i in indices:
        dictionary[word[:1]] = i + 1
    else:
        dictionary[word[:2]] = i + 1

print(dictionary)
