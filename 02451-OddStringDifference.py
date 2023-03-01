# https://leetcode.com/problems/odd-string-difference/description/

class Solution:
    def oddString(self, words: List[str]) -> str:
        """
        Logic: Hash Map

        Time: O(n)
        Space: O(n)
        """
        hash_map = collections.defaultdict(list)

        for word in words:
            diff = []
            for i in range(1, len(word)):
                diff.append(ord(word[i]) - ord(word[i-1]))
            hash_map[tuple(diff)].append(word)
        
        for k, v in hash_map.items():
            if len(v) == 1:
                return v[0]

        return None
