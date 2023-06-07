# https://leetcode.com/problems/shortest-way-to-form-string/description

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        """
        Logic: Two Pointers
        
        Time: O(s*t)
        Space: O(1)
        """
        for t in target:
            if t not in source:
                return -1
            
        i, j = 0, 0
        res = 1
        
        while i < len(target):
            if j >= len(source):
                j = 0
                res += 1
            if target[i] == source[j]:
                i += 1
            j += 1
        
        return res
