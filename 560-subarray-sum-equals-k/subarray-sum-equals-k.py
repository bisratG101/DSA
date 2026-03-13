class Solution(object):
    def subarraySum(self, nums, k):
        prefix = 0
        count = {0:1}
        res = 0

        for n in nums:
            prefix += n
            if prefix - k in count:
                res += count[prefix - k]

            count[prefix] = count.get(prefix, 0) + 1

        return res
