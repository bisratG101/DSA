class Solution:
    def romanToInt(self, s: str) -> int:

        values=  {
            "M" : 1000 , "D" : 500 , "C" : 100,
            "L" : 50 , "X" : 10 , "V" : 5
            ,"I": 1
        }
        total = 0
        for i in range (len(s)):
            if i < len(s)-1 and values[s[i]] < values[s[i+1]]:
                total-=values[s[i]]
            else :
                total+=values[s[i]]
        return total










        # values = {
        #     'I': 1, 'V': 5, 'X': 10,
        #     'L': 50, 'C': 100,
        #     'D': 500, 'M': 1000
        # }
        
        # total = 0
        
        # for i in range(len(s)):
        #     if i < len(s) - 1 and values[s[i]] < values[s[i+1]]:
        #         total -= values[s[i]]
        #     else:
        #         total += values[s[i]]
                
        # return total
