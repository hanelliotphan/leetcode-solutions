# https://leetcode.com/problems/number-of-arithmetic-triplets/description/

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        """
        Logic: Brute Force
        
        Time: O(n^2)
        Space: O(1)
        """
        count = 0

        for n in nums:
            if n+diff in nums and n+2*diff in nums:
                count += 1
        
        return count
