class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        best_answer = nums[0]
        answer = nums[0]
        for i in range(1,n):
            v1 = best_answer + nums[i]
            v2 = nums[i]
            best_answer = max(v1,v2)
            answer = max(best_answer,answer)
        return answer