class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        def atMost(k):
            count = {}
            left = 0
            res = 0

            for right in range(len(nums)):
                count[nums[right]] = count.get(nums[right], 0) + 1

                if count[nums[right]] == 1:
                    k -= 1

                while k < 0:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        k += 1
                    left += 1

                res += right - left + 1

            return res

        return atMost(k) - atMost(k-1)
