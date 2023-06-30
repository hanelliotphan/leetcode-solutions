# https://leetcode.com/problems/day-of-the-year/description/

class Solution:
    def dayOfYear(self, date: str) -> int:
        """
        Logic: Brute Force with Lear Year consideration

        Time: O(1)
        Space: O(1)
        """
        days_per_month = {
            1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
            7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
        }
        
        def leap_year(year):
            if year % 4 == 0:
                if year % 100 == 0 and year % 400 == 0:
                    return True
                elif year % 100 == 0 and year % 400 != 0:
                    return False
                elif year % 4 == 0:
                    return True
            return False
        
        y, m, d = date.split("-")

        if leap_year(int(y)):
            days_per_month[2] += 1
        
        if m == "01":
            return int(d)
        
        count = 0
        
        for i in range(1, int(m)):
            count += days_per_month[i]
        
        return count + int(d)
