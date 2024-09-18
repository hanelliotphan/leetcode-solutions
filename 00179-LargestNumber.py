class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        """
        Logic: Sorting by lex order

        Time: O(n*logn)
        Space: O(n)
        """
        nums.sort(key=lambda x: str(x)*10, reverse=True)

        if str(nums[0]) == "0":
            return "0"

        return "".join([str(x) for x in nums])
