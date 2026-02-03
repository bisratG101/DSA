class Solution:
    def isPalindrome(self, x: int) -> bool:
        n=x
        sum1 = 0
        while(x>0):
            sum1=(sum1*10) + (x%10) 
            x=x//10
        return sum1==n


    