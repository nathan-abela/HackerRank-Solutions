# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/prng-sequence-guessing/problem
# Difficulty: Medium
# Max Score: 50
# Language: Python

# ========================
#         Solution
# ========================

def updateSeed(seed):
    #  n * 25214903917 -> is 0x5DEECE66D in hex
    return (seed * 0x5DEECE66D + 0xB) & ((1 << 48) - 1)

def shiftSeed(seed):
    return seed >> 17

def nextInt(seed, n):
    return shiftSeed(seed) % n

def findSeed(values):
    for lower_bits in range(2 ** 20):
        seed = lower_bits

        for value in values:
            seed = updateSeed(seed)

            if (shiftSeed(seed) & 7) - (value & 7):
                break
        else:
            for higher_bits in range(2 ** 28):
                seed = lower_bits | (higher_bits << 20)

                for value in values:
                    seed = updateSeed(seed)

                    if nextInt(seed, 1000) != value:
                        break
                else:
                    return seed

for _ in range(int(input())):
    values = list(map(int, input().split()))
    seed = findSeed(values)
    result = list()

    for _ in range(10):
        seed = updateSeed(seed)
        result.append(nextInt(seed, 1000))

    print(' '.join(map(str, result)))
