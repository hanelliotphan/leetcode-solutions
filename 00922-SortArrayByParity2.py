class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        """
        Logic: Brute Force
        
        Time: O(n)
        Space: O(n)
        """
        odds = []
        evens = []
        
        for n in nums:
            if n % 2 == 0:
                evens.append(n)
            else:
                odds.append(n)
                
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = evens[-1]
                evens.pop()
            else:
                nums[i] = odds[-1]
                odds.pop()
                
        return nums
