class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        res =""
        for i in range(len(indices)):
            index = indices.index(i)
            res += s[index]

        return res

























        # n = len(s)
        # result = [""] * n
        
        # for i in range(n):
        #     result[indices[i]] = s[i]
        
        # return "".join(result)
