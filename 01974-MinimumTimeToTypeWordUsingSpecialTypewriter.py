class Solution:
    def minTimeToType(self, word: str) -> int:
        """
        Logic: Greedy
        
        Time: O(n)
        Space: O(1)
        """
        num_sec = len(word)
        prev_char = "a"
        
        for ch in word:
            num_turn = (ord(ch) - ord(prev_char)) % 26
            num_sec += min(num_turn, 26-num_turn)
            prev_char = ch
            
        return num_sec
