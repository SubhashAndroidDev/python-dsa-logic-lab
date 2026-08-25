# 6. Zigzag Conversion
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        t = list(range(numRows)) + list(range(numRows - 2, 0, -1))

        r = [''] * numRows

        for i, char in enumerate(s):
            r[t[i % len(t)]] += char

        return ''.join(r)


print(Solution().convert("PAYPALISHIRING", 3))