class Solution:
    from collections import defaultdict
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
    
        
        count_map = defaultdict(int)
        
        for entry in cpdomains:
            count_str, domain = entry.split()
            count = int(count_str)
            
            parts = domain.split('.')
            
           
            for i in range(len(parts)):
                subdomain = ".".join(parts[i:])
                count_map[subdomain] += count
        
      
        result = []
        for domain, total in count_map.items():
            result.append(f"{total} {domain}")
        
        return result
