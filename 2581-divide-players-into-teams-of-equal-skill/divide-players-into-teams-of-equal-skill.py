class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        target = 0
        n = len(skill)
        if n ==2:
            return skill[0]*skill[1]
        for i in skill:
            target+=i
        if (target % (n//2)) != 0:
            return -1
        ans = 0
        left = 0 
        right = n-1
        target = (target) // (n/2) 
        skill = sorted(skill)
        while(left<right):
            if skill[left]+ skill[right] == target:
                ans+= skill[left]*skill[right]
            else :
                return -1
            left+=1
            right-=1
        return ans 

        








        # target = 0
        # n = len(skill)
        # if n ==2:
        #     return skill[0]*skill[1]
        # for i in skill:
        #     target+=i
        # if (target % (n//2)) != 0:
        #     return -1
        # target = (target) // (n/2)       
        # ans = 0
        # for i in range(len(skill)):
        #     if skill[i] == 0: continue      
        #     b =False 
        #     for j in range(i+1 , n):                              
        #         if skill[i]+skill[j] == target:
        #             ans+=(skill[i]*skill[j])
        #             skill[j]=0
        #             b=True
        #             break
        #     if not b:
        #         return -1
        # return ans 


        