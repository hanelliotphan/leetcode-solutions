# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Logic: Two pointers
        
        Time: O(n)
        Space: O(1)
        """
        max_water = 0
        l = 0
        r = len(height)-1
        
        while l < r:
            area = (r-l) * min(height[l], height[r])
            max_water = max(max_water, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return max_water
