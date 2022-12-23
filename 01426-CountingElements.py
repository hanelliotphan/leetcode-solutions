# https://leetcode.com/problems/counting-elements/description/

class Solution:
    def countElements(self, arr: List[int]) -> int:
        """
        Logic: Straightforward
        
        Time: O(n)
        Space: O(1)
        """
        count = 0
        
        for i in arr:
            if i + 1 in arr:
                count += 1
                
        return count
