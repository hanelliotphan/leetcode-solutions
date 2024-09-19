class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        """
        Logic: Brute Force

        Time: O(n)
        Space: O(n)
        """
        st = ""

        for word in words:
            st += word[0]
        
        return st == s
