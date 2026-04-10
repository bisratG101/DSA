class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        mp = {}

        for num in nums2:
            while stack and num > stack[-1]:
                mp[stack.pop()] = num
            stack.append(num)

        for num in stack:
            mp[num] = -1

        return [mp[num] for num in nums1]