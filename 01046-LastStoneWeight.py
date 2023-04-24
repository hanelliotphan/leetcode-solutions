# https://leetcode.com/problems/last-stone-weight/description/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        Logic: Brute Force
        
        Time: O(n*logn)
        Space: O(1)
        """
        if len(stones) == 1:
            return stones[0]
        
        stones.sort()

        while len(stones) > 0:
            s1 = stones.pop()
            s2 = stones.pop()
            if abs(s1-s2) != 0:
                stones.append(abs(s1-s2))
            if len(stones) == 1:
                break
            stones.sort()
        
        return stones[0] if len(stones) == 1 else 0
