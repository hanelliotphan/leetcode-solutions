# https://leetcode.com/problems/jewels-and-stones/description/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        """
        Logic: Hash Map/Counter
        
        Time: O(j)
        Space: O(s)
        """
        stone_counter = collections.Counter(stones)
        res = 0

        for j in jewels:
            res += stone_counter[j]
        
        return res
