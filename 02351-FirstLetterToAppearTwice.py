class Solution:
    def repeatedCharacter(self, s: str) -> str:
        """
        Logic: Hash Map
        
        Time: O(n)
        Space: O(n)
        """
        hash_map = dict()
        
        for ch in s:
            if ch not in hash_map:
                hash_map[ch] = 1
            else:
                hash_map[ch] += 1
            if hash_map[ch] == 2:
                return ch
            
        return None
