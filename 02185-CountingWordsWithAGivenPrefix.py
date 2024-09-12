class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        """
        Logic: Brute Force

        Time: O(n*k)
        Space: O(1)
        """
        count = 0
        
        for word in words:
            if word[:len(pref)] == pref:
                count += 1
        
        return count
