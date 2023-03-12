# https://leetcode.com/problems/largest-odd-number-in-string/description/

class Solution:
    def largestOddNumber(self, num: str) -> str:
        """
        Logic: Brute Force

        Time: O(n)
        Space: O(1)
        """
        n = len(num)
        res = ""
        
        for i in range(n-1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[:i+1]
        
        return res
