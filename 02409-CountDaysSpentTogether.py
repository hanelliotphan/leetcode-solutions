# https://leetcode.com/problems/count-days-spent-together/

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        """
        Logic: Total Days in Year
        
        Time: O(1) --> loop through 12 months
        Space: O(1) --> 12-month size hash map
        """
        month_days_map = {
            1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
            7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
        }
        
        amA, adA = arriveAlice.split("-")
        lmA, ldA = leaveAlice.split("-")
        amB, adB = arriveBob.split("-")
        lmB, ldB = leaveBob.split("-")
        
        num_days_arrive_Alice = sum([month_days_map[i] for i in range(1, int(amA))]) + int(adA)
        num_days_leave_Alice = sum([month_days_map[i] for i in range(1, int(lmA))]) + int(ldA)
        nums_day_arrive_Bob = sum([month_days_map[i] for i in range(1, int(amB))]) + int(adB)
        nums_day_leave_Bob = sum([month_days_map[i] for i in range(1, int(lmB))]) + int(ldB)
                
        arrive_time = max(num_days_arrive_Alice, nums_day_arrive_Bob)
        leave_time = min(num_days_leave_Alice, nums_day_leave_Bob)
        
        return leave_time - arrive_time + 1 if leave_time >= arrive_time else 0
