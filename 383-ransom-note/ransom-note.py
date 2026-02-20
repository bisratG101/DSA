class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        r = Counter(ransomNote)
        m = Counter(magazine)
        for ch in r:
            if r[ch] > m[ch]:
                return False
        return True
