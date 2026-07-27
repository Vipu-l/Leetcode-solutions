class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low = 0
        window_sum = 0
        minLen = float('inf')

        for high in range(len(nums)):
            window_sum += nums[high]

            while window_sum >= target:
                minLen = min(minLen, high - low + 1)
                window_sum -= nums[low]
                low += 1

        return 0 if minLen == float('inf') else minLen
        