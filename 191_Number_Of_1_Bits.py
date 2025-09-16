
from collections import Counter

def hammingWeight(n: int) -> int:
    return bin(n)[2:].count("1")

print(hammingWeight(11))
print(hammingWeight(128))
print(hammingWeight(2147483645))
