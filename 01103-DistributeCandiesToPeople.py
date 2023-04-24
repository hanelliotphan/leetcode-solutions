# https://leetcode.com/problems/distribute-candies-to-people/description/

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        """
        Logic: Brute Force
        
        Time: O(candies)
        Space: O(1)
        """
        people = [0] * num_people
        i = 0
        curr_candies = 1

        while candies > 0:
            if i == num_people:
                i = 0
            people[i] += curr_candies
            candies -= curr_candies
            curr_candies = min(curr_candies+1, candies)
            i += 1
        
        return people
