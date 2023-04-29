# https://leetcode.com/problems/meeting-rooms/description/

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """
        Logic: Brute Force with Sort
        
        Time: O(n*logn)
        Space: O(1)
        """
        if len(intervals) <= 1:
            return True
        
        intervals.sort(key=lambda x: x[0])
        curr_start = intervals[0][0]

        for start, end in intervals:
            if curr_start > start:
                return False
            curr_start = end
        
        return True
