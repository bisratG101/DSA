class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        ans = []
        result = set()

        for i in nums:
            if i in result:
                ans.append(i)
            else :
                result.add(i)
        return ans 

        
        