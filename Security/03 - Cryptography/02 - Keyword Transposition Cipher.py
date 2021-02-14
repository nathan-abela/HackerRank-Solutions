# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/keyword-transposition-cipher/problem
# Difficulty: Easy
# Max Score: 50
# Language: Python

# ========================
#         Solution
# ========================

from string import ascii_uppercase as aaa

def decode(k, m):
    # Removes duplicates from key
    key = ''.join([x for i, x in enumerate(k) if k.index(x) == i])

    # Get aplhabet without chars in key
    alph = ''.join([x for x in aaa if x not in key])

    # Get base ordered char
    dec = key + alph

    # Creates columns by indexing: range() with steps of len(key) and
    # Increases the start-value from 0 to len(key) + sorts them
    columns = sorted([''.join([dec[x] for x in
                               range(n, len(dec), len(key))])
                      for n in range(len(key))])

    # Creates a decoding dict
    d = {a: b for b, a in zip(aaa, ''.join(columns))}

    # Decode
    return ''.join(d[x] if x in d else ' ' for x in m)

for _ in range(int(input())):
    key = input()
    mes = input()

    print(decode(key, mes))
