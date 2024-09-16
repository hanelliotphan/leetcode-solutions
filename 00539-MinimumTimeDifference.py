class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        """
        Logic: Brute Force with Sorting

        Time: O(n*logn)
        Space: O(1) -- re-using the `timePoints` input
        """
        min_diff = float("inf")
        timePoints = [int(t.split(":")[0])*60+int(t.split(":")[1]) for t in timePoints]
        timePoints.sort()

        for i in range(1, len(timePoints)):
            min_diff = min(min_diff, timePoints[i]-timePoints[i-1])
        
        return min(min_diff, 1440-timePoints[-1]+timePoints[0])
