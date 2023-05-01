class Solution:
    def average(self, salary: List[int]) -> float:
        """
        Logic: Brute Force
        
        Time: O(n)
        Space: O(1)
        """
        mx = max(salary)
        mn = min(salary)

        return (sum(salary) - mx - mn) / (len(salary)-2)
