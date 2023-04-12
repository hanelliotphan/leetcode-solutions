# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/description/

class Solution:
    def minDeletions(self, s: str) -> int:
        """
        Logic: Hash Map/Counter

        Time: O(n)
        Space: O(n)
        """
        counter = collections.Counter(s)
        visited = set()
        deletions = 0
        
        for count in counter.values():
            while count > 0 and count in visited:
                count -= 1
                deletions += 1
            visited.add(count)
        
        return deletions
