# https://leetcode.com/problems/calculate-delayed-arrival-time/

class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        """
        Logic: Brute Force
        
        Time: O(1)
        Space: O(1)
        """
        if arrivalTime + delayedTime >= 24:
            return arrivalTime + delayedTime - 24
        else:
            return arrivalTime + delayedTime
