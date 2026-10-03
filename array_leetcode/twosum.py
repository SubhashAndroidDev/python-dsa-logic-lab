class Solution:
    def twosum(self,nums,target):
        seen={}
        for i, num in enumerate(nums):
            complement=target-num
            if complement in seen:
                return [seen[complement],i]
            seen[num]=i
            
            
print(Solution().twosum([2,7,11,15],9))            
    