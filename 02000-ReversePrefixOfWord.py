# https://leetcode.com/problems/reverse-prefix-of-word/description/

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        """
        Logic: Brute Force

        Time: O(n)
        Space: O(1)
        """
        for i in range(len(word)):
            if ch == word[i]:
                return word[:i+1][::-1] + word[i+1:]
        
        return word
