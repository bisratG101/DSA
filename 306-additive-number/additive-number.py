class Solution(object):
    def isAdditiveNumber(self, num):
        n = len(num)
        
        # Try all splits for first and second number
        for i in range(1, n):
            for j in range(i+1, n):
                
                a = num[:i]
                b = num[i:j]
                
                # Skip leading zeros
                if (a[0] == '0' and len(a) > 1) or (b[0] == '0' and len(b) > 1):
                    continue
                
                if self.isValid(a, b, num[j:]):
                    return True
        
        return False

    def isValid(self, a, b, remaining):
        while remaining:
            c = str(int(a) + int(b))
            
            if not remaining.startswith(c):
                return False
            
            remaining = remaining[len(c):]
            a, b = b, c
        
        return True