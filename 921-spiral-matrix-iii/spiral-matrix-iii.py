class Solution:
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        res = []
        r, c = rStart, cStart
        res.append([r, c])
        
        step = 1
        while len(res) < rows * cols:
            
            # move east
            for _ in range(step):
                c += 1
                if 0 <= r < rows and 0 <= c < cols:
                    res.append([r, c])
            
            # move south
            for _ in range(step):
                r += 1
                if 0 <= r < rows and 0 <= c < cols:
                    res.append([r, c])
            
            step += 1
            
            # move west
            for _ in range(step):
                c -= 1
                if 0 <= r < rows and 0 <= c < cols:
                    res.append([r, c])
            
            # move north
            for _ in range(step):
                r -= 1
                if 0 <= r < rows and 0 <= c < cols:
                    res.append([r, c])
            
            step += 1
        
        return res