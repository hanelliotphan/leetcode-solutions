class Solution:
    def countAsterisks(self, s: str) -> int:
        """
        Logic: Straightforward slicing
        
        Time: O(n)
        Space: O(1)
        """
        return ''.join(s.split('|')[::2]).count('*')
