# https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/description/

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        """
        Logic: Brute Force
        
        Time: O(n)
        Space: O(1)
        """
        count = 0
        
        for i in range(len(startTime)):
            if startTime[i] <= queryTime and endTime[i] >= queryTime:
                count += 1
        
        return count
