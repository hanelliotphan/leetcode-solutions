# https://leetcode.com/problems/sentence-similarity/description/

class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        """
        Logic: Brute Force

        Time: O(n*k)
        Space: O(1)
        """
        if len(sentence1) != len(sentence2):
            return False

        for i in range(len(sentence1)):
            if not(sentence1[i] == sentence2[i] or [sentence1[i], sentence2[i]] in similarPairs or [sentence2[i], sentence1[i]] in similarPairs):
                return False

        return True
