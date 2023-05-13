# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        """
        Logic: Brute Force
        
        Time: O(n)
        Space: O(1)
        """
        x = 0

        for op in operations:
            if op[:2] == "--" or op[-2:] == "--":
                x -= 1
            else:
                x += 1
        
        return x
