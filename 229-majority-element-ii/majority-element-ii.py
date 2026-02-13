class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
       
        n =len(nums)
        count1 = 0
        count2 =0 
        ele1 = -100000004
        ele2 = -100000004
        ans = []
        for i in range(len(nums)):
            if count1 ==0 and ele2!=nums[i]:
                ele1= nums[i]
                count1 =1
            elif count2 == 0 and ele1 != nums[i]:
                ele2 = nums[i]
                count2 =1
            elif ele1==nums[i]: count1+=1
            elif ele2 == nums[i]: count2+=1
            else :
                count1 -=1
                count2 -=1
        count1= 0
        count2 = 0
        for i in range(len(nums)):
            if nums[i] == ele1: count1 +=1
            if nums[i] == ele2 : count2 +=1
        
        if count1 > n/3: ans.append(ele1)
        if count2 > n/3 : ans.append(ele2)
        return ans 


        
        
       











        # n=len(nums)
        # # Better solution 
        # mp= {}
        # ans = []
        # for i in range(len(nums)):
        #     if nums[i] not in  mp:
        #         mp[nums[i]]=0
        #     mp[nums[i]]+=1
        # for key , value in mp.items():
        #     if value > n/3: 
        #         ans.append(key)

        # return ans 









        # Brute Force
        # ans =[]
        # for i in range(len(nums)):
        #     count =0    
        #     for j in range(len(nums)):
        #         if nums[i]==nums[j]:
        #             count+=1
        #     if count > len(nums)/3:
        #         if nums[i] not in ans : 
        #             ans.append(nums[i])
        # return ans
        

        