class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != min(nums) and nums[i] != max(nums):
                return nums[i]
        for i in range(len(nums)-1):
            if nums[i] == min(nums) and nums[i+1] == max(nums):
                return -1
        return -1