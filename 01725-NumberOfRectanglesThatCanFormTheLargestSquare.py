# https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        """
        Logic: Hash Map
        
        Time: O(n)
        Space: O(n)
        """
        hash_map = {}
        max_len = 0
        
        for a, b in rectangles:
            sq_len = min(a, b)
            max_len = max(max_len, sq_len)
            if sq_len not in hash_map:
                hash_map[sq_len] = 1
            else:
                hash_map[sq_len] += 1
                
        return hash_map[max_len]
