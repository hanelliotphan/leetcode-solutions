class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        """
        Logic: Mathematical Approach

        Time: O(k)
        Space: O(1)
        """
        if k % 2 == 0:
            return -1

        curr_num = 0
        for digit_one in range(1, k+1):
            curr_num = (curr_num * 10 + 1) % k
            if curr_num == 0:
                return digit_one
        
        return -1
