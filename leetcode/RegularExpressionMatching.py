class Solution:

    def isMatch(self, s: str, p: str) -> bool:

        m = len(s)
        n = len(p)

        dp = [[False] * (n + 1) for _ in range(m + 1)]

        dp[m][n] = True

        for i in range(m, -1, -1):
            for j in range(n - 1, -1, -1):

                first_match = (
                    i < m and
                    (s[i] == p[j] or p[j] == '.')
                )

                if j + 1 < n and p[j + 1] == '*':

                    zero_occurrences = dp[i][j + 2]

                    one_or_more = (
                        first_match and dp[i + 1][j]
                    )

                    dp[i][j] = zero_occurrences or one_or_more

                else:
                    dp[i][j] = (
                        first_match and dp[i + 1][j + 1]
                    )

        return dp[0][0]


# Create object
solution = Solution()

# Test cases
print(solution.isMatch("aa", "a"))
print(solution.isMatch("aa", "a*"))
print(solution.isMatch("ab", ".*"))