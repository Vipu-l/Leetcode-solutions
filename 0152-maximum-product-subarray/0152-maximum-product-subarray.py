class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        minending = nums[0]
        maxending = nums[0]
        result = nums[0]
        for i in range(1,n):
            v1 = nums[i]
            v2 = minending * nums[i]
            v3 = maxending * nums[i]
            maxending = max(v1,max(v2,v3))
            minending = min(v1,min(v2,v3))
            result = max(result,max(minending,maxending))
        return result