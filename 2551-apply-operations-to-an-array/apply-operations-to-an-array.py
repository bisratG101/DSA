class Solution(object):
    def applyOperations(self, s):
        """
        :type nums: List[int]
        :rtype: List[int]
        """


        for i in range(len(s)):
            if i+1<len(s) and s[i]==s[i+1]:
                s[i]*=2
                s[i+1]=0
        i = 0
        right = i+1
        while(right<len(s) and i < len(s)):
            if s[right]==0:
                right+=1
                continue 
            if s[i] ==0:
                s[i],s[right]=s[right],s[i]
                i+=1
                right+=1
            else:
                i+=1
                right=i+1
                
        return s