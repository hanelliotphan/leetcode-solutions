# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        """
        Logic: Brute Force
        
        Time: O(1)
        Space: O(1)
        """
        return root.left.val + root.right.val == root.val
