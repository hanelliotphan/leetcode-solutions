# https://leetcode.com/problems/determine-if-two-strings-are-close/

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        """
        Logic: Counter Hash Map
        
        Time: O(n)
        Space: O(n)
        """
        counter1_freqs = collections.Counter(word1).values()
        counter2_freqs = collections.Counter(word2).values()
        
        set1 = set(word1)
        set2 = set(word2)
        
        return Counter(counter1_freqs) == Counter(counter2_freqs) and set1 == set2
