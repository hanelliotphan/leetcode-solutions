# https://leetcode.com/problems/thousand-separator/description/

class Solution:
    def thousandSeparator(self, n: int) -> str:
        """
        Logic: Brute Force

        Time: O(logd(n))
        Space: O(1)
        """
        if n < 1000:
            return str(n)
        
        s = ""
        n_copy = n
        i = 0

        while n_copy > 0:
            d = n_copy % 10
            s += str(d)
            i += 1
            if i == 3:
                s += "."
                i = 0
            n_copy //= 10
        
        return s[::-1] if s[-1] != "." else s[:-1][::-1]
