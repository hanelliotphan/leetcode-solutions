# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        """
        Logic: Depth First Search
        
        Time: O(n)
        Space: O(1)
        """
        if not root: return 0
        self.result = 0
        
        def dfs(node, curr_max, curr_min):
            if not node: return 0
            self.result = max(self.result,
                           abs(curr_max-node.val),
                           abs(curr_min-node.val))
            curr_max = max(node.val, curr_max)
            curr_min = min(node.val, curr_min)
            dfs(node.left, curr_max, curr_min)
            dfs(node.right, curr_max, curr_min)
        
        dfs(root, root.val, root.val)
        
        return self.result
