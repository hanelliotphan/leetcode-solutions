class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Logic: Hash Map/Counter
        
        Time: O(n)
        Space: O(n)
        """        
        cs = collections.Counter(s)

        for ch in t:
            if ch not in cs:
                return False
            cs[ch] -= 1

        for v in cs.values():
            if v != 0:
                return False
        
        return True
