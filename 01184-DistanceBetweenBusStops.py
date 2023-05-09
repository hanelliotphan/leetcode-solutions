# https://leetcode.com/problems/distance-between-bus-stops/description/

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        """
        Logic: Brute Force
        
        Time: O(n)
        Space: O(1)
        """
        a = min(start, destination)
        b = max(start, destination)

        return min(sum(distance[a:b]), sum(distance)-sum(distance[a:b]))
