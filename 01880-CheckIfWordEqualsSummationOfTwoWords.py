class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        """
        Logic: Brute Force
        
        Time: O(f+s+t)
        Space: O(1)
        """
        fwn = swn = twn = ""
        
        for ch in firstWord:
            fwn += str((ord(ch) - ord('a')))
        
        for ch in secondWord:
            swn += str((ord(ch) - ord('a')))
            
        for ch in targetWord:
            twn += str((ord(ch) - ord('a')))
            
        return True if int(fwn) + int(swn) == int(twn) else False
