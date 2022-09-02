# https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        Logic: Binary Format
        
        Time: O(1)
        Space: O(1)
        """
        return "{0:b}".format(int(a, 2) + int(b, 2))
