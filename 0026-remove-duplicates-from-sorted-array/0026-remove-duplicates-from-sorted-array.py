class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        count = 1;
        low = 0;
        high = 1;
        for high in range(1,n):
            if(nums[high]==nums[high-1]):
                high += 1
            else:
                nums[low+1] = nums[high]
                count += 1
                low += 1
                high += 1
        return count
    