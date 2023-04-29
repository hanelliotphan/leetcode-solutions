# https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/description/

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        """
        Logic: Hash Map/Counter
        
        Time: O(n)
        Space: O(n)
        """
        counter = collections.Counter(arr)

        for k, v in counter.items():
            if v > len(arr)//4:
                return k
        
        return None
