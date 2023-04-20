# https://leetcode.com/problems/count-common-words-with-one-occurrence/description/

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        """
        Logic: Hash Map/Counter
        
        Time: O(m+n)
        Space: O(m+n)
        """
        c1 = collections.Counter(words1)
        c2 = collections.Counter(words2)

        visited = set()

        for k, v in c1.items():
            if k in words2 and v + c2[k] == 2:
                visited.add(k)
        
        for k, v in c2.items():
            if k in words1 and v + c1[k] == 2:
                visited.add(k)
    
        return len(visited)
