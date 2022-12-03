# https://leetcode.com/problems/sort-characters-by-frequency/

class Solution:
    def frequencySort(self, s: str) -> str:
        """
        Logic: Hash Map
        
        Time: O(n*logn)
        Space: O(n)
        """
        lookup = {}
        
        for c in s:
            if c not in lookup:
                lookup[c] = 1
            else:
                lookup[c] += 1
                
        lookup = sorted(lookup.items(), key=lambda x: -x[1])
        res = ""
        
        for k, v in lookup:
            res += (k*v)
            
        return res
