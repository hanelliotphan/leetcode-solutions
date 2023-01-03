# https://leetcode.com/problems/jewels-and-stones/description/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        """
        Logic: Hash Map/Counter
        
        Time: O(j)
        Space: O(max(s, j))
        """
        j = collections.Counter(jewels)
        s = collections.Counter(stones)
        count = 0
        
        for k in j.keys():
            if k in s.keys():
                count += s[k]
                
        return count
