class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Logic: Hash Map
            - Store the occurrences of characters in `s` and `t`
            - in a hash map then compare the value at the character key.
            - If equal, return True, if not equal return False
            
        Time: O(n)
        Space: O(n)
        """        
        if len(s) != len(t):
            return False
        
        hash_s, hash_t = {}, {}
        
        for i in range(len(s)):
            hash_s[s[i]] = hash_s.get(s[i], 0) + 1
            hash_t[t[i]] = hash_t.get(t[i], 0) + 1
            
        for c in hash_s:
            if hash_s[c] != hash_t.get(c):
                return False
            
        return True
