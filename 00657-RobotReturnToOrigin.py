# https://leetcode.com/problems/robot-return-to-origin/

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        """
        Logic: Brute Force
        
        Time: O(n)
        Space: O(1)
        """
        points = {"U": 1, "D": -1, "L": -1, "R": 1}
        x = 0
        y = 0
        
        for move in moves:
            if move in "UD": y += points[move]
            elif move in "LR": x += points[move]
            
        return x == 0 and y == 0
