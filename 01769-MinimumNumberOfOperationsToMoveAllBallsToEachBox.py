# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        """
        Logic: Dynamic Programming
        
        Time: O(n)
        Space: O(n)
        """
        n = len(boxes)

        left = [0] * n
        left_moves = int(boxes[0])
        for i in range(1, n):
            left[i] = left[i-1] + left_moves
            left_moves += int(boxes[i])
        
        right = [0] * n
        right_moves = int(boxes[-1])
        for i in range(n-2, -1, -1):
            right[i] = right[i+1] + right_moves
            right_moves += int(boxes[i])
        
        res = [0] * n
        for i in range(n):
            res[i] = left[i] + right[i]
        
        return res
