# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Logic: Recursion

        Time: O(n)
        Space: O(1) --> required to return O(n) data, no extra space is needed
        """
        if not root: return []
        res = []

        def recurse(node, curr_level):
            if len(res) == curr_level:
                res.append([])
            res[curr_level].append(node.val)
            if node.left:
                recurse(node.left, curr_level+1)
            if node.right:
                recurse(node.right, curr_level+1)
        
        recurse(root, 0)
        
        return res[::-1]
