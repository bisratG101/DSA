class Solution:
    def minimumIndex(self, nums: list[int]) -> int:
        
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        total = nums.count(candidate)
        left_count = 0
        n = len(nums)
        
        for i in range(n - 1):
            if nums[i] == candidate:
                left_count += 1
            if left_count * 2 > (i + 1) and (total - left_count) * 2 > (n - i - 1):
                return i
        return -1
