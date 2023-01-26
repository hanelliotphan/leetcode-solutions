class Solution:
    def alternateDigitSum(self, n: int) -> int:
        """
        Logic: Brute Force

        Time: O(n)
        Space: O(1)
        """
        res = 0
        start = 1
        if len(str(n)) % 2 == 0: start = -1

        while n > 0:
            d = divmod(n, 10)[1]
            res += (d * start)
            start *= (-1)
            n //= 10

        return res
