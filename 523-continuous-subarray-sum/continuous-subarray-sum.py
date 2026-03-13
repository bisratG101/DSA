class Solution(object):
    def checkSubarraySum(self, nums, k):
        mod = {0: -1}
        prefix = 0

        for i in range(len(nums)):
            prefix = (prefix + nums[i]) % k

            if prefix in mod:
                if i - mod[prefix] > 1:
                    return True
            else:
                mod[prefix] = i

        return False
