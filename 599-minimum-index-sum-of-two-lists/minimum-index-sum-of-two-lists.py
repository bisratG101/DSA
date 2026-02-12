class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        

        sumi = 2001
        result = []
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i]==list2[j]:
                    if i+j < sumi:
                        sumi = i+j
                        result = []
                        result.append(list1[i])
                    elif i+j == sumi:
                        result.append(list1[i])
        return result 


        


        

       
