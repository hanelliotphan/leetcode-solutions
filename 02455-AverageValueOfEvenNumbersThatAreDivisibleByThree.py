# https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/

class Solution:
    def averageValue(self, nums: List[int]) -> int:
        """
        Logic: Brute Force
        
        Time: O(n)
        Space: O(1)
        """
        count = total = 0
        
        for n in nums:
            if n % 6 == 0:
                total += n
                count += 1
                
        return total // count if count > 0 else 0
