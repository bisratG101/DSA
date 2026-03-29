class Solution(object):
    def maxPathSum(self, root):
        self.max_sum = float('-inf')
        
        def dfs(node):
            if not node:
                return 0
            
            # Ignore negative paths
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            
            # Try path passing through this node
            self.max_sum = max(self.max_sum, left + right + node.val)
            
            # Return best single path to parent
            return node.val + max(left, right)
        
        dfs(root)
        return self.max_sum