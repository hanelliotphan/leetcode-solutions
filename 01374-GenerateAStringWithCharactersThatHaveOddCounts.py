class Solution:
    def generateTheString(self, n: int) -> str:
        """
        Logic: Brute Force
        
        Time: O(1)
        Space: O(1)
        """
        if n % 2 == 0:
            return "a"*(n-1) + "b"
        else:
            if n > 1:
                return "a"*(n-2)+"b"+"c"
            else:
                return "a"
