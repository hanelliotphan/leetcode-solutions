class Solution:
    def removeVowels(self, s: str) -> str:
        """
        Logic: Brute Force
        
        Time: O(n)
        Space: O(n)
        """
        return "".join([ch for ch in s if ch not in "aeiou"])
