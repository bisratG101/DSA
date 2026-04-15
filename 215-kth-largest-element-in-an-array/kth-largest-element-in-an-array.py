import random

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k = len(nums) - k  
        
        def quickselect(left, right):
            if left == right:
                return nums[left]
            
            pivot = nums[random.randint(left, right)]
            
           
            l, i, r = left, left, right
            
            while i <= r:
                if nums[i] < pivot:
                    nums[l], nums[i] = nums[i], nums[l]
                    l += 1
                    i += 1
                elif nums[i] > pivot:
                    nums[i], nums[r] = nums[r], nums[i]
                    r -= 1
                else:
                    i += 1
            
           
            
            if k < l:
                return quickselect(left, l - 1)
            elif k > r:
                return quickselect(r + 1, right)
            else:
                return nums[k]
        
        return quickselect(0, len(nums) - 1)
        
        