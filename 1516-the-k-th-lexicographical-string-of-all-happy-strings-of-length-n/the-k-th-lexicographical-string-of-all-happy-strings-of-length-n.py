class Solution(object):
    def getHappyString(self, n, k):
        res = []
        
        def backtrack(path):
            if len(res) >= k:
                return
            if len(path) == n:
                res.append("".join(path))
                return
            
            for ch in ['a', 'b', 'c']:
                if not path or path[-1] != ch:
                    path.append(ch)
                    backtrack(path)
                    path.pop()
        
        backtrack([])
        return res[k - 1] if k <= len(res) else ""