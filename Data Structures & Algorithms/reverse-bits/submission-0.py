class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        for i in range(32):
            bit = n & 1
            bit <<= (32 - i - 1)
            result = result | bit
            n >>= 1
        return result