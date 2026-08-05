class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)

        low = 0

        for high in range(1, n):
            if nums[high] != nums[low]:
                low += 1
                nums[low] = nums[high]

        return low + 1