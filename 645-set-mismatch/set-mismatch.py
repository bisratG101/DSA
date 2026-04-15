class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        duplicate = -1
        missing = -1
        
        for num in nums:
            index = abs(num) - 1
            
            if nums[index] < 0:
                duplicate = abs(num)
            else:
                nums[index] = -nums[index]
        
        for i in range(len(nums)):
            if nums[i] > 0:
                missing = i + 1
        
        return [duplicate, missing]