#User function Template for python3
from collections import Counter
class Solution:
    #Function to check if a is a subset of b.
    
    def isSubset(self, a, b):
        # Your code here
        countA = Counter(a)
        countB=  Counter(b)
        
        for i in range (len(b)):
            if countB[b[i]] > countA[b[i]]:
                return False  
        return True 
        
        
        # for i in range(len(b)):
        #     c = False 
        #     for j in range(len(a)):
        #         if b[i]==a[j]:
        #             a[j]=-1
        #             c=True
        #             break
        #     if c==False: return False 
        # return True 
                
      
    
    
