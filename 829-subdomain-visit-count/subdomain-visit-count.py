class Solution:
    from collections import defaultdict
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        mp = {}
        ans = []
        for site in cpdomains:
            web= site.split(" ")
            num = int(web[0])
            sites=web[1]
            webs=sites.split(".")
            cp = ""
            for i in range(len(webs)-1,-1,-1):
                if i != len(webs)-1:
                    cp=  webs[i]+"."+cp
                else:
                    cp= webs[i]
                mp[cp] = mp.get(cp,0)+num
        for key , value in mp.items():
            strs = str(value)+" "+key
            ans.append(strs)
        return ans



    
        
        
