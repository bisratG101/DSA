class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)  
    
        sorted_keys = sorted(freq, key=lambda x: freq[x], reverse=True)
        return sorted_keys[:k]
