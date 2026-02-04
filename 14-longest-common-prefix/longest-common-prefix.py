class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        res = ""
        prefix= strs[0]
        for i in range(len(prefix)):
            for j in strs:
                if i== len(j) or j[i] !=  prefix[i]:
                    return res
            res+=prefix[i]
        return res 
            

        # strs.sort()
        # first = strs[0]
        # last = strs[len(strs)-1]
        # res = ""
        # for i in range(len(first)):
        #     if first[i] == last[i]:
        #         res+=first[i]
        #     else : return res
        # return res 


        
        
        
        

                
        