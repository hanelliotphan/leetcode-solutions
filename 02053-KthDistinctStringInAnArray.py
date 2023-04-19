# https://leetcode.com/problems/kth-distinct-string-in-an-array/description/

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        """
        Logic: Hash Map/Counter
        
        Time: O(n)
        Space: O(n)
        """
        counter = collections.Counter(arr)

        for n, freq in counter.items():
            if freq == 1:
                k -= 1
            if not k:
                return n
        
        return ""
