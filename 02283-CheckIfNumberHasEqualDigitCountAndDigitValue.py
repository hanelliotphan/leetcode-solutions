# https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/description/

class Solution:
    def digitCount(self, num: str) -> bool:
        """
        Logic: Hash Map/Counter

        Time: O(n)
        Space: O(n)
        """
        counter = collections.Counter(num)

        for i in range(len(num)):
            if counter[str(i)] != int(num[i]):
                return False
        
        return True 
