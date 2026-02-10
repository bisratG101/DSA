class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(len(nums)):
            for j in range(i+1 , len(nums)):
                if nums[i]+nums[j]==target:
                    return i , j
        




        


        # num_map = {}

        # for i in range (len(nums)):
        #     check = target - nums[i]
        #     if nums[i] in num_map : return num_map[nums[i]] , i

        #     num_map[check] = i 

        # return [] 












        # for i in range (len(nums)):
        #     for j in range(i+1 ,  len(nums)):
        #         if nums[i] + nums[j] == target: return i , j 


        # return []






















        # num_map = {}

        # for i in range (len(nums)):
        #     check = target-nums[i]
        #     if nums[i] in num_map: 
        #          return [num_map[nums[i]] , i]
            
        #     num_map[check]= i

        # return []



        
        # for i in range (len(nums)):
        #     for j in range (i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i, j]
                
        # return []
                
        