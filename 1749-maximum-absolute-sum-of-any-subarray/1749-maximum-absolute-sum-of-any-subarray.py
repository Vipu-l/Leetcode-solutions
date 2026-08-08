class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n = len(nums)
        def maxSum(nums) -> int:
            bestEnd = nums[0]
            res = nums[0]
            for i in range(1,n):
                v1 = nums[i]
                v2 = nums[i] + bestEnd
                bestEnd = max(v1,v2)
                res = max(res,bestEnd)
            return abs(res)
        def minSum(nums) -> int:
            bestEnd = nums[0]
            res = nums[0]
            for i in range(1,n):
                v1 = nums[i]
                v2 = nums[i] + bestEnd
                bestEnd = min(v1,v2)
                res = min(res,bestEnd)
            return abs(res)
        return max(maxSum(nums),minSum(nums))