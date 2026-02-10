class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        map = {}
        for i in range(len(nums)):
            if nums[i] not in map:
                map[nums[i]] = 0
            map[nums[i]]+=1

                
        for i in range(len(nums)):
            if map[nums[i]]==1: return nums[i]
        
        


          
     