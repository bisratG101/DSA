class Solution(object):
    def findSubsequences(self, nums):
        res = set()
        
        def backtrack(start, path):
            if len(path) >= 2:
                res.add(tuple(path))
            
            for i in range(start, len(nums)):
                if not path or nums[i] >= path[-1]:
                    path.append(nums[i])
                    backtrack(i + 1, path)
                    path.pop()
        
        backtrack(0, [])
        return list(map(list, res))