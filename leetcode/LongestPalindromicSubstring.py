class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start, end = 0, 0  # indices of the best palindrome found

        def expand(left: int, right: int) -> tuple[int, int]:
            # Expand outward while characters match
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # left, right are now one step past the valid palindrome
            return left + 1, right - 1

        for i in range(len(s)):
            # Odd-length palindromes (single center)
            l1, r1 = expand(i, i)
            if r1 - l1 > end - start:
                start, end = l1, r1

            # Even-length palindromes (center between i and i+1)
            l2, r2 = expand(i, i + 1)
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end + 1]


# longestPalindrome("babad")
print(Solution().longestPalindrome("babad"))

    