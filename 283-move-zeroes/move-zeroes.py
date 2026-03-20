class Solution(object):
    def moveZeroes(self, s):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
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

