# https://leetcode.com/problems/shortest-completing-word/description/

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        """
        Logic: Hash Map/Counter
        
        Time: O(l)
        Space: O(l+w)
        """
        lcounter = collections.Counter(ch.lower() for ch in licensePlate if ch.isalpha())
        shortest_word = ""
        shortest_len = float("inf")

        for word in words:
            if not lcounter - collections.Counter(word):
                if len(word) < shortest_len:
                    shortest_word = word
                    shortest_len = len(word)
        
        return shortest_word
