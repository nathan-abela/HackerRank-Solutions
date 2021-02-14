# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/basic-cryptanalysis/problem
# Difficulty: Hard
# Max Score: 50
# Language: Python

# ========================
#         Solution
# ========================

import re

f = open('dictionary.lst', 'r')
data = f.read().lower()
f.close()

words = data.split()
wordmap = {}

for word in words:
    length = len(word)
    sub = wordmap.get(length, {})
    wordmap[length] = sub

    gen = ''
    for c in word:
        if c not in gen:
            gen += c

    key = [0] * length
    for i, c in enumerate(word):
        key[i] = gen.index(c)
    key = ' '.join([str(k) for k in key])

    arr = sub.get(key, [])
    sub[key] = arr

    arr.append(word)

alpha = 'abcdefghijklmnopqrstuvwxyz'
cypher = ['.'] * 26
data = input()
enc = data.split()
test = enc[:]

def cycle():
    global test, cypher, alpha, wordmap

    for word in test:
        length = len(word)

        gen = ''
        for c in word:
            if c not in gen:
                gen += c

        key = [0] * length
        pattern = ''

        for i, c in enumerate(word):
            key[i] = gen.index(c)
            try:
                j = cypher.index(c)
                pattern += alpha[j]
            except:
                pattern += '.'
        key = ' '.join([str(k) for k in key])

        matches = wordmap[length][key]
        copy = []

        for match in matches:
            if re.fullmatch(pattern, match):
                copy.append(match)

        matches = copy

        if len(matches) == 1:
            test.remove(word)
            match = matches[0]
            for i in range(length):
                x = alpha.index(match[i])
                cypher[x] = word[i]

i = len(test)

while True:
    cycle()
    j = len(test)
    if i == j:
        break
    i = j

cypher = ''.join(cypher)
out = [' '] * len(data)

for i, c in enumerate(data):
    if c is not ' ':
        out[i] = alpha[cypher.index(c)]

print(''.join(out))
