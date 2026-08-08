class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        def maxNotCircular(nums) -> int:
            bestEnd = nums[0]
            res = nums[0]
            for i in range(1,n):
                v1 = nums[i]
                v2 = nums[i] + bestEnd
                bestEnd = max(v1,v2)
                res = max(res,bestEnd)
            return res
        def maxCircular(nums) -> int:
            bestEnd = nums[0]
            res = nums[0]
            for i in range(1,n):
                v1 = nums[i]
                v2 = nums[i] + bestEnd
                bestEnd = min(v1,v2)
                res = min(res,bestEnd)
            total = sum(nums)
            if total == res:
                return maxNotCircular(nums)
            result = total - res
            return result
        return max(maxNotCircular(nums),maxCircular(nums))