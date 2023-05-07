# https://leetcode.com/problems/index-pairs-of-a-string/description/

class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        """
        Logic: Brute Force
        
        Time: O(t*w)
        Space: O(1)
        """
        res = []

        for word in words:
            for i in range(len(text)-len(word)+1):
                if text[i:i+len(word)] == word:
                    res.append([i, i+len(word)-1])
        
        return sorted(res, key=lambda x: [x[0], x[1]])
