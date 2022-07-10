class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Logic: Hash Map
        
        Time: O(n)
        Space: O(n)
        """
        indices = {}
        
        for i in range(len(nums2)):
            if nums2[i] not in indices:
                indices[nums2[i]] = i
                
        return [indices[n] for n in nums1]
