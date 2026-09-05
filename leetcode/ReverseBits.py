"""You are given a 32-bit unsigned integer. Reverse its bits and return the resulting integer.

Input:  43261596
Output: 964176192

Input:
00000010100101000001111010011100

Reverse:
00111001011110000010100101000000
"""

class Solution:

    def reverseBits(self, n: int) -> int:
        result = 0

        for _ in range(32):
            bit = n & 1
            result = (result << 1) | bit

            n >>= 1

        return result


print(Solution().reverseBits(43261596))
