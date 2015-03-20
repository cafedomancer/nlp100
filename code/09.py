sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

result = []

for word in sentence.split():
    if len(word) > 4:
        result.append('TODO')
    else:
        result.append(word)

result = ' '.join(result)

print(result)
