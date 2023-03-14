# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        Logic: Preorder Traversal

        Time: O(n)
        Space: O(h)
        """
        def preorder_traverse(node, num):
            nonlocal total_sum
            if node:
                num = num*10 + node.val
                if not node.left and not node.right:
                    total_sum += num
                preorder_traverse(node.left, num)
                preorder_traverse(node.right, num)

        total_sum = 0
        preorder_traverse(root, 0)
        
        return total_sum
