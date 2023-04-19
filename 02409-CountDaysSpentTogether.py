# https://leetcode.com/problems/count-days-spent-together/

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        """
        Logic: Total Days in Year
        
        Time: O(1) --> loop through 12 months
        Space: O(1) --> 12-month size hash map
        """
        md_map = {
            1: 31, 2: 28, 3: 31, 4: 30,
            5: 31, 6: 30, 7: 31, 8: 31,
            9: 30, 10: 31, 11: 30, 12: 31
        }

        amA, adA = arriveAlice.split("-")
        num_arrive_A = sum([md_map[i] for i in range(1, int(amA))]) + int(adA)

        lmA, ldA = leaveAlice.split("-")
        num_leave_A = sum([md_map[i] for i in range(1, int(lmA))]) + int(ldA)

        amB, adB = arriveBob.split("-")
        num_arrive_B = sum([md_map[i] for i in range(1, int(amB))]) + int(adB)

        lmB, ldB = leaveBob.split("-")
        num_leave_B = sum([md_map[i] for i in range(1, int(lmB))]) + int(ldB)

        arrive_day = max(num_arrive_A, num_arrive_B)
        leave_day = min(num_leave_A, num_leave_B)

        if arrive_day > leave_day:
            return 0

        return leave_day - arrive_day + 1
