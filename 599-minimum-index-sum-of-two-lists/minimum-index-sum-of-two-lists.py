class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        mp = {}
        minI = 2001
        ans = []

        for i in range(len(list1)):
            mp[list1[i]] = i
        for i in range(len(list2)):
            if list2[i] in mp:
                n = mp[list2[i]] + i
                if n < minI:
                    ans.clear()
                    ans.append(list2[i])
                    minI = n
                elif n == minI:
                    ans.append(list2[i])
        return ans






        



        

        

        
        
        
        
        
        
        # sumi = 2001
        # result = []
        # for i in range(len(list1)):
        #     for j in range(len(list2)):
        #         if list1[i]==list2[j]:
        #             if i+j < sumi:
        #                 sumi = i+j
        #                 result = []
        #                 result.append(list1[i])
        #             elif i+j == sumi:
        #                 result.append(list1[i])
        # return result 


        


        

       
