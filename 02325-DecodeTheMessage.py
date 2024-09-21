class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        """
        Logic: Hash Map
        
        Time: O(m+n)
        Space: O(m)
        """
        hash_map = {" ": " "}
        curr = ord('a')
        res = ''

        for k in key:
            if k not in hash_map:
                hash_map[k] = chr(curr)
                curr += 1
            
        for m in message:
            res += hash_map[m]
        
        return res
