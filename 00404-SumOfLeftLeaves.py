# https://leetcode.com/problems/sum-of-left-leaves/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        """
        Logic: Depth First Search
        
        Time: O(n)
        Space: O(1)
        """
        res = 0

        def dfs(node):
            nonlocal res
            if not node:
                return
            if node.left and not node.left.left and not node.left.right:
                res += node.left.val
            dfs(node.left)
            dfs(node.right)
        
        if not root: return 0
        dfs(root)
        return res
