class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return (len(nums) * (len(nums) + 1))//2 - sum(nums)

        # nums.sort()

        # for i in range(len(nums)):
        #     if nums[i] != i:
        #         return i
        
        # return nums[len(nums)-1]+1
        