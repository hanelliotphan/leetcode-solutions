# https://leetcode.com/problems/ransom-note/description/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Logic: Hash Map/Counter
        
        Time: O(r)
        Space: O(max(r, m))
        """
        c1 = collections.Counter(ransomNote)
        c2 = collections.Counter(magazine)
        
        for k, v in c1.items():
            if v > c2[k]:
                return False
            
        return True
