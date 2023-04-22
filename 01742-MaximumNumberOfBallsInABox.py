# https://leetcode.com/problems/maximum-number-of-balls-in-a-box/description/

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        """
        Logic: Hash Map/Counter
        
        Time: O(n)
        Space: O(n)
        """
        box_start = 1
        box_counter = collections.defaultdict(int)
        max_box = 0

        for n in range(lowLimit, highLimit+1):
            d = 0
            while n > 0:
                d += n % 10
                n //= 10
            box_counter[d] += 1
            max_box = max(max_box, box_counter[d])
        
        return max_box
