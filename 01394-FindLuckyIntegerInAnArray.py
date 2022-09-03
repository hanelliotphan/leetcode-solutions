# https://leetcode.com/problems/find-lucky-integer-in-an-array/

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        """
        Logic: Counter
        
        Time: O(n)
        Space: O(n)
        """
        counter = collections.Counter(arr)
        max_lucky_number = -1
        
        for k, v in counter.items():
            if k == v:
                max_lucky_number = max(max_lucky_number, k)
                
        return max_lucky_number
