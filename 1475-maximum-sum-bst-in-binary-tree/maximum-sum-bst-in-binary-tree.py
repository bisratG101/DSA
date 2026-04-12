# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxSumBST(self, root):
        self.max_sum = 0
        
        def dfs(node):
            if not node:
                return (True, float('inf'), float('-inf'), 0)
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if left[0] and right[0] and left[2] < node.val < right[1]:
                curr_sum = left[3] + right[3] + node.val
                self.max_sum = max(self.max_sum, curr_sum)
                return (True, min(left[1], node.val), max(right[2], node.val), curr_sum)
            
            return (False, 0, 0, 0)
        
        dfs(root)
        return self.max_sum
        