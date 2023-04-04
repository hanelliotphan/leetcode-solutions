# https://leetcode.com/problems/take-gifts-from-the-richest-pile/description/

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        """
        Logic: Brute Force with Sort

        Time: O(n*logn)
        Space: O(1) --> re-utilize `gifts` array
        """
        for _ in range(k):
            gifts.sort(reverse=True)
            gifts[0] = int(math.sqrt(gifts[0]))
        
        return sum(gifts)
