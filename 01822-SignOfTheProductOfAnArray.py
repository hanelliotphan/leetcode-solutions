# https://leetcode.com/problems/sign-of-the-product-of-an-array/description/

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        """
        Logic: Mathematical Approach -- Compute number of negative numbers
        
        Time: O(n)
        Space: O(1)
        """
        neg = 0

        for n in nums:
            if n == 0: return 0
            elif n < 0: neg += 1
        
        return 1 if neg % 2 == 0 else -1
