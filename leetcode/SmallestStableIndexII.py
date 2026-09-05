class Solution:
    def firstStableIndex(self, nums, k):
        n = len(nums)

        # minFromIndex[i] = minimum element from i to n-1
        minFromIndex = [0] * n

        minEl = float("inf")

        for i in range(n - 1, -1, -1):
            minEl = min(minEl, nums[i])
            minFromIndex[i] = minEl

        # max element from 0 to i
        maxEl = float("-inf")

        for i in range(n):
            maxEl = max(maxEl, nums[i])

            if maxEl - minFromIndex[i] <= k:
                return i

        return -1

print(Solution().firstStableIndex([1, 3, 6, 4, 1, 2], 2))    