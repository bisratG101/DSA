class Solution:
    from collections import Counter
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        sumLength = 0
        for word in words:
            b= True
            for ch in word:
                n = word.count(ch)
                m = chars.count(ch)
                if n > m:
                    b = False
                    break 
            if b:
                sumLength += len(word)
        return sumLength
            

        
        
        
        
        
        
        # mp = Counter(chars)
        # count = 0   
        # nowmp = {}     

        # for line in words:
        #     nowmp.clear()
        #     nowmp = Counter(line)
        #     b = True 
        #     counter= 0 
        #     for i in range(len(line)):
        #         if mp[line[i]] <nowmp[line[i]]:
        #             b=False
        #             break
        #         else:
        #             counter+=1
        #     if b:
        #         count+=counter
        # return count










        