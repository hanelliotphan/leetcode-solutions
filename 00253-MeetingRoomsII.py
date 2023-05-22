# https://leetcode.com/problems/meeting-rooms-ii/description/

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        Logic: Brute Force (get the net sum of rooms based on valid start time and end time)
        
        Time: O(n*logn)
        Space: O(n)
        """
        if not intervals: return 0

        start = end = 0
        needed_rooms = 0

        start_times = sorted([x[0] for x in intervals])
        end_times = sorted([x[1] for x in intervals])

        while start < len(intervals):
            if start_times[start] >= end_times[end]:
                end += 1
                needed_rooms -= 1
            start += 1
            needed_rooms += 1
        
        return needed_rooms
