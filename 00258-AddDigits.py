class Solution:
    def addDigits(self, num: int) -> int:
        """
        Logic: Brute Force
        
        Time: O(n)
        Space: O(1)
        """
        n_copy = num
        curr_d = 0

        while n_copy > 0 or curr_d >= 10:
            curr_d += n_copy % 10
            n_copy //= 10
            if n_copy == 0 and curr_d >= 10:
                n_copy = curr_d
                curr_d = 0
        
        return curr_d
