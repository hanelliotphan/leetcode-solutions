# https://leetcode.com/problems/convert-the-temperature/

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        """
        Logic: Brute Force
        
        Time: O(1)
        Space: O(1)
        """
        return [celsius+273.15, celsius*1.80+32.00]
