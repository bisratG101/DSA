class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        mp ={}
        ans = []

        for ana in strs:
            sorts = "".join(sorted(ana))
            mp.setdefault(sorts,[]).append(ana)
        for value in mp.values():
            ans.append(value)
       
            
        return ans 


        