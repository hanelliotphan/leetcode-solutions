class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        """
        Logic: Straightforward
        
        Time: O(n)
        Space: O(n)
        """
        l1 = nums[:n]
        l2 = nums[n:]
        res = []
        
        for i in range(n):
            res.extend([l1[i], l2[i]])
        
        return res
