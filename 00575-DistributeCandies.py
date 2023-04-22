# https://leetcode.com/problems/distribute-candies/description/

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        """
        Logic: Mathematical Approach with Set
        
        Time: O(n)
        Space: O(n)
        """
        return min(len(set(candyType)), len(candyType)//2)
