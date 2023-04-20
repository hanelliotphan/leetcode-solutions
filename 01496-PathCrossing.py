# https://leetcode.com/problems/path-crossing/

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        """
        Logic: Brute Force with Set

        Time: O(n)
        Space: O(n)
        """
        x = 0
        y = 0
        visited = {(x, y)}

        for direction in path:
            if direction == "N":
                y += 1
            elif direction == "S":
                y -= 1
            elif direction == "E":
                x += 1
            elif direction == "W":
                x -= 1
            if (x, y) in visited:
                return True
            visited.add((x, y))
        
        return False
