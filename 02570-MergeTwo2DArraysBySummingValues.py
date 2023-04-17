# https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/description/

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        """
        Logic: Hash Map

        Time: O((n+m)*log(n+m))
        Space: O(n+m)
        """
        res = []
        counter = collections.defaultdict(int)

        for id, val in nums1:
            counter[id] += val
        
        for id, val in nums2:
            counter[id] += val
        
        for k, v in counter.items():
            res.append([k, v])
        
        return sorted(res, key=lambda x: x[0])
