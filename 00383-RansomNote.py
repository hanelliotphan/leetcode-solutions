# https://leetcode.com/problems/ransom-note/description/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Logic: Hash Map/Counter
        
        Time: O(r)
        Space: O(r+m)
        """
        if len(ransomNote) > len(magazine):
            return False

        ransom_count = collections.Counter(ransomNote)
        mag_count = collections.Counter(magazine)

        for k, v in ransom_count.items():
            if mag_count[k] < v:
                return False
        
        return True
