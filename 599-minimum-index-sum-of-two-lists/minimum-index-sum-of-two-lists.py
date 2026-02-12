class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        mp = {}
        sumi = 2001
        ans = []
       
        for i , v in enumerate(list1):
            mp[v] =i

        for i in range(len(list2)):
            if list2[i] in list1:
                indexSum = i + mp[list2[i]]
                if indexSum < sumi:
                    ans=[]
                    ans.append(list2[i])
                    sumi = indexSum
                elif  indexSum == sumi:
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


        


        

       
