class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        Logic: Recursion

        Time: O(n)
        Space: O(1)
        """
        if n == 0:
            return 1
        elif n < 0:
            x = 1/x
            n = -n
        
        curr_step = 1
        res = x

        while curr_step * 2 < n:
            curr_step *= 2
            res *= res
        
        return res * self.myPow(x, n-curr_step)
