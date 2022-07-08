class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        """
        Logic: Hash Map
        
        Time: O(m+n)
        Space: O(m)
        """
        key_mapping = dict()
        key_str = ''.join(key.split(" "))
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        idx = 0
        
        for k in key_str:
            if k not in key_mapping:
                key_mapping[k] = alphabet[idx]
                idx += 1
                
        decoded_msg = ""
        for m in message:
            if m == " ":
                decoded_msg += m
            else:
                decoded_msg += key_mapping[m]
            
        return decoded_msg
