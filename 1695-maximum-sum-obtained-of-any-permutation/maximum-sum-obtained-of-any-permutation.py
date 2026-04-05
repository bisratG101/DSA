class Solution(object):
    def maxSumRangeQuery(self, nums, requests):
        MOD = 10**9 + 7
        n = len(nums)
        
        count = [0] * (n + 1)
        
        for start, end in requests:
            count[start] += 1
            if end + 1 < n:
                count[end + 1] -= 1
        
      
        for i in range(1, n):
            count[i] += count[i - 1]
        
        count = count[:n]
        
      
        nums.sort()
        count.sort()
        
      
        result = 0
        for i in range(n):
            result = (result + nums[i] * count[i]) % MOD
        
        return result