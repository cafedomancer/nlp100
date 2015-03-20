import re

def cipher(string):
    return re.sub(r'[a-z]',
                  lambda matchobj: chr(219 - ord(matchobj.group(0))),
                  string)

print(cipher('I am an NLPer'))
print(cipher(cipher('I am an NLPer')))
