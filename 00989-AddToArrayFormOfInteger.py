# https://leetcode.com/problems/add-to-array-form-of-integer/description/

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        """
        Logic: Go from right to left of the string, add `k`
                to the unit digit of the `num` array, then keep track
                of carry to continue to add to the next digits of `num`
        
        Time: O(max(n, log k))
        Space: O(max(n, logk))
        """
        res = []
        i = len(num) - 1
        
        while k > 0 or i >= 0:
            total = k
            total += num[i] if i >=0 else 0
            k, r = divmod(total, 10)
            res.append(r)
            i -= 1
            
        return res[::-1]
