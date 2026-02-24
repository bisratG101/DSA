class Solution:
    from collections import Counter
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = Counter(nums)

        count  =sorted(count.items(), key= lambda x : x[1], reverse=True)
        ans = []
        for value , key in count:
            ans.append(value)
            k -=1
            if k ==0:
                break
        return ans 


      


            




        



















        # freq = Counter(nums)  
    
        # sorted_keys = sorted(freq, key=lambda x: freq[x], reverse=True)
        # return sorted_keys[:k]
