class Solution:
    def reverseBits(self, n: int) -> int:
        for i in range(16):
            if (n >> (31-i)) & 1 != (n >> i) & 1: 
                n ^= 1 << (31-i) | 1 << i
        return n