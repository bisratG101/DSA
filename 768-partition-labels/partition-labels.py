class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: list[int]
        """
   
        last = {}
        for i, c in enumerate(s):
            last[c] = i
        
        result = []
        start = end = 0
        
        
        for i, c in enumerate(s):
            end = max(end, last[c])  
            if i == end:            
                result.append(end - start + 1)
                start = i + 1
        
        return result
