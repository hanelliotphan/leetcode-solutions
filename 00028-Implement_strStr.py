class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Logic: Take the length of needle and loop through 
                each position of haystack and find if it matches
                
        Time: O(n)
        Space: O(1)
        """
        # Base case: needle is empty, no need to find
        if not needle: return 0
        
        n = len(needle)
        
        for i in range(len(haystack)):
            if haystack[i:i+n] == needle:
                return i
            
        return -1
