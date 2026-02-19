class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        count = Counter(s)
        return ''.join(ch * freq for ch, freq in sorted(count.items(), key=lambda x: -x[1]))
