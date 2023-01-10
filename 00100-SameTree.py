# https://leetcode.com/problems/same-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Logic: Depth First Search

        Time: O(n)
        Space: O(1)
        """
        def dfs(p, q):
            if not p and not q:
                return True
            elif (p and not q) or (q and not p):
                return False
            elif q.val != p.val:
                return False
            else:
                return dfs(p.left, q.left) and dfs(p.right, q.right)
        
        return dfs(p, q)
