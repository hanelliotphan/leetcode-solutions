class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Logic: Hash Map
        
        Time: O(m+n)
        Space: O(n)
        """
        indices = collections.defaultdict(int)

        for i, n in enumerate(nums2):
            indices[n] = i
        
        res = []
        
        for n in nums1:
            res.append(indices[n])
        
        return res
