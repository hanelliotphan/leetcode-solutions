# https://leetcode.com/problems/largest-odd-number-in-string/description/

class Solution:
    def largestOddNumber(self, num: str) -> str:
        """
        Logic: Brute Force (find the rightmost odd digit)
        
        Time: O(n)
        Space: O(1)
        """
        for i in range(len(num)-1, -1, -1):
            if int(num[i]) % 2:
                return num[:i+1]
        
        return ""
