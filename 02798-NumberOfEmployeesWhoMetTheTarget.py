class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        """
        Logic: Brute Force

        Time: O(n)
        Space: O(1)
        """
        return sum(hr >= target for hr in hours)
