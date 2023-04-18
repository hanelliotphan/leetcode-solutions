class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        """
        Logic: Brute Force
        
        Time: O(max(a^2+b^2, a^2+c^2, b^2+c^2))
        Space: O(1)
        """
        res = []

        for n in nums1:
            if n in nums2:
                res.append(n)
            if n in nums3:
                res.append(n)
        
        for n in nums2:
            if n in nums3:
                res.append(n)
        
        return list(set(res))
