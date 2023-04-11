# https://leetcode.com/problems/palindrome-number/description/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Logic: Brute Force

        Time: O(n)
        Space: O(1)
        """
        if x < 0:
            return False
        
        new_x = 0
        x_copy = x

        while x_copy:
            new_x = new_x*10 + x_copy%10
            x_copy //= 10

        return new_x == x
