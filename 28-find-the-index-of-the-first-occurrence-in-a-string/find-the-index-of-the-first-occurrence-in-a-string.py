class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        
        for j in range(len(haystack)):
            i = 0
            b= False
            index = j
            while i < len(needle) and index <len(haystack) :
                if haystack[index] != needle[i]:
                    break
                if i == len(needle)-1:
                    b = True
                index+=1
                i+=1
            if b :
                return j
        return -1
               
            
        




            


        