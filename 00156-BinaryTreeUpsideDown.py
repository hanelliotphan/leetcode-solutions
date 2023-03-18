# https://leetcode.com/problems/binary-tree-upside-down/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Logic: Iteration

        Time: O(n)
        Space: O(n)
        """
        curr = root
        prev = node = None

        while curr:
            curr.right, curr.left, curr, prev, node = prev, node, curr.left, curr, curr.right

        return prev
