class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        return len(nums) != len(set(nums))



        








        # other Solution 
        # "seen = []
        # for i in range(len(nums)):
        #     if nums[i] in seen:
        #         return True 
        #     seen.append(nums[i])
        # return False "



        #  Better Solution 
        # count = {}
        # for i in range(len(nums)):
        #     if nums[i] not in count:
        #         count[nums[i]] = 0
        #     count[nums[i]]+=1
        # for i in range(len(nums)):
        #     if count[nums[i]] >= 2:
        #         return True
        # return False  



        # Brute Fource 
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[j]==nums[i]:
        #             return True
        # return False 

        