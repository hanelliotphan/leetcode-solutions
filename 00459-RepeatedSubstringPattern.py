class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """
        Logic: Take a substring of s and check when it's duplicated
                by len(s) // i, it can be equal to s
                
        Time: O(n*sqrt(n))
        Space: O(n)
        """
        n = len(s)
        
        for i in range(1, n//2+1):
            if n % i == 0 and s[:i]*(n//i) == s:
                return True
            
        return False
