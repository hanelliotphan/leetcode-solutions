class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        """
        Logic: Hash Map

        Time: O(n*logn)
        Space: O(n)
        """
        id_sum = {}
        res = []

        for id, val in nums1:
            if id not in id_sum:
                id_sum[id] = val
            else:
                id_sum[id] += val

        for id, val in nums2:
            if id not in id_sum:
                id_sum[id] = val
            else:
                id_sum[id] += val

        for k, v in id_sum.items():
            print([k, v])
            res.append([k, v])

        return sorted(res, key=lambda x: x[0])
