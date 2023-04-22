# https://leetcode.com/problems/intersection-of-three-sorted-arrays/description/

class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        """
        Logic: Brute Force
        
        Time: O((a+b+c)*log(a+b+c))
        Space: O(a+b+c)
        """
        return sorted(list(set(arr1) & set(arr2) & set(arr3)))
