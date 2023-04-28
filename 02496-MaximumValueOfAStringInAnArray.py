# https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/description/

class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        """
        Logic: Brute Force
        
        Time: O(n)
        Space: O(1)
        """
        max_val = 0 

        for s in strs:
            if s.isnumeric():
                max_val = max(max_val, int(s))
            else:
                max_val = max(max_val, len(s))
        
        return max_val
