# https://leetcode.com/problems/destination-city/description/

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        """
        Logic:
        
        Time: O(n)
        Space O(n)
        """
        src_cities = set()
        dest_cities = set()

        for src, dest in paths:
            src_cities.add(src)
            dest_cities.add(dest)
        
        return [x for x in (dest_cities-src_cities)][0]
