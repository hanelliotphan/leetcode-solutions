class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Logic: Two Pointers
        
        Time: O(n)
        Space: O(1)
        """
        i = 0

        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        
        return i
