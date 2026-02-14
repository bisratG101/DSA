class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:

        mp = {}
        ans = []

        for path in paths:
            fileN = path.split(" ")
            dic= fileN[0]
           
            for line in fileN[1:]:
                pos = line.index("(")
                content= line[pos+1:-1]
                txt = line[:pos]
                pathfull=dic+"/"+txt
                mp.setdefault(content, []).append(pathfull)
        
        for k in mp:
            if len(mp[k]) >=2:
                ans.append(mp[k])
        return ans 


                

        

        

        