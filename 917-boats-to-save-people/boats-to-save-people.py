class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        if n ==1: return 1 

        left = 0
        right = n-1
        boat = 0
        people = sorted(people)
        while left <=right:
            if people[right]+people[left] <=limit:
                left+=1
            right-=1
            boat+=1
        return boat
        



        # n = len(people)
        # if n ==1: return 1 

        # left = 0
        # right = n-1
        # boat = 0
        # people = sorted(people)
        # while(left < right ):
        #     if people[right]==limit or people[right]+people[left] >limit :
        #         boat+=1
        #         right-=1
        #     else:
        #         boat+=1
        #         right-=1
        #         left+=1
                
        # if left==right : boat+=1
        # return boat 









        # n = len(people)
        # if n ==1: return 1 

        # people = sorted(people)
        # ans = 0
        # i = 0
        # while i < n:
        #     full = 0
            
        #     for j in range(i,n):
        #         full+=people[j]
        #         if full == limit or j<n-1 and full+people[j+1] > limit :
        #             break               
        #     i = j 
        #     ans+=1
        #     if people[i] >=limit:
        #         break
        # if i!=n-1:
        #     ans+= (n-i)+1
        # return ans 

        # left =0 
        # right = 1
        # while right < n:
        #     full = 0
        #    while full<limt:
        #     if full == limt:
                
        #     full+=people[left]        