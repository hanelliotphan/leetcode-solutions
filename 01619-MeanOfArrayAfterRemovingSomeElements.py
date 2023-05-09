# https://leetcode.com/problems/mean-of-array-after-removing-some-elements/description/

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        """
        Logic: Brute Force with Sort
        
        Time: O(n*logn)
        Space: O(1)
        """
        arr.sort()
        p = ceil(0.05*len(arr))

        while p != 0:
            arr.pop(0)
            arr.pop()
            p -= 1

        return sum(arr) / len(arr)
