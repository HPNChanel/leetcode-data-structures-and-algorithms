
def reverseBits(n: int) -> int:
    n &= 0xFFFFFFFF                    # ép về 32-bit unsigned
    rev = 0
    for _ in range(32):
        rev = (rev << 1) | (n & 1)
        n >>= 1

    return rev if rev < (1 << 31) else rev - (1 << 32)

print(reverseBits(43261596))
print(reverseBits(2147483644))
