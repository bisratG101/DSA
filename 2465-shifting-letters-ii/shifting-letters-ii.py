class Solution(object):
    def shiftingLetters(self, s, shifts):
        n = len(s)
        diff = [0] * (n + 1)
        
        for start, end, direction in shifts:
            if direction == 1:  
                diff[start] += 1
                diff[end + 1] -= 1
            else: 
                diff[start] -= 1
                diff[end + 1] += 1
      
        for i in range(1, n):
            diff[i] += diff[i - 1]
        
        result = []
        for i in range(n):
            shift = diff[i] % 26
            new_char = (ord(s[i]) - ord('a') + shift) % 26
            result.append(chr(new_char + ord('a')))

        return "".join(result)