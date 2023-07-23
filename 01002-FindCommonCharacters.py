# https://leetcode.com/problems/find-common-characters/description/

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        """
        Logic: Brute Force

        Time: O(n)
        Space: O(100) --> O(1)
        """
        res = []

        for ch in set(words[0]):
            count = []
            for word in words:
                count.append(word.count(ch))
            res += ch * min(count)
        
        return res
