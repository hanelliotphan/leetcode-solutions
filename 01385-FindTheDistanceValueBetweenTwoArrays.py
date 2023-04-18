# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/description/

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        """
        Logic: Binary Search
        
        Time: O(n*logm)
        Space: O(1)
        """
        arr2.sort()
        count = 0
        
        def find_distance_value(n):
            l, r = 0, len(arr2)
            while l < r:
                mid = (l+r) // 2
                if abs(arr2[mid]-n) <= d:
                    return False
                elif arr2[mid] > n:
                    r = mid
                else:
                    l = mid + 1
            return True

        for n in arr1:
            count += find_distance_value(n)
        
        return count
