class Solution(object):

    def countOdds(self, low, high):
        return (high + 1) // 2 - (low // 2)


solution = Solution()

result = solution.countOdds(3, 7)

print(result)