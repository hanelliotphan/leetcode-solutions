# https://leetcode.com/problems/find-all-the-lonely-nodes/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        """
        Logic: Depth First Search
        
        Time: O(n)
        Space: O(1)
        """
        if not root:
            return []
        
        res = []

        def helper(node):
            if not node.left and node.right:
                res.append(node.right.val)
            if node.left and not node.right:
                res.append(node.left.val)
            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)
        
        helper(root)
        return res
