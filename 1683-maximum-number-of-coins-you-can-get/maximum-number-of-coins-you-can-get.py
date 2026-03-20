class Solution(object):
    def maxCoins(self, piles):
        piles.sort()
        res = 0
        left = 0
        right = len(piles) - 1
        
        while left < right:
            right -= 1
            res += piles[right]
            right -= 1
            left += 1
        
        return res