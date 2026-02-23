class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ 

        # Optimal solution useing two pointer

        i = 0
        for j in range(len(nums)):            
            if nums[j] != 0:
                nums[i] , nums[j] = nums[j] , nums[i]
                i+=1
        return nums
















        # i = 0 
        # for j in range(len(nums)):
        #     if nums[j]!=0:
        #         nums[i] , nums[j] = nums[j] , nums[i]
        #         i+=1
        # return nums















        # Burte-Force solution 

        # temp = []
        # for i in range(len(nums)):
        #     if nums[i]!=0:
        #         temp.append(nums[i])
        # for i in range(len(nums)):
        #     if i <=len(temp)-1:
        #         nums[i]=temp[i]
        #     else:
        #         nums[i]=0
        # return nums 
        




    






    
        # # if len(nums) == 1: return nums

        # # j = 0
        
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         nums[j] , nums[i] = nums[i] , nums[j]
        #         j+=1
        # return nums


        
            
            
           
        # return nums



        
        # for i in range(len(nums)):
        #     if(nums[i]==0):
        #         for j in range (i+1 , len(nums)):
        #             if nums[j]!=0:
        #                 nums[i] , nums[j] = nums[j] , nums[i]
        #                 break 
        

        # return nums