class Solution(object):
    def minimumReplacement(self, nums):
        res = 0
        prev = nums[-1]
        
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= prev:
                prev = nums[i]
            else:
                parts = (nums[i] + prev - 1) // prev
                res += parts - 1
                prev = nums[i] // parts
        
        return res