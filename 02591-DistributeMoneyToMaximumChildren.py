# https://leetcode.com/problems/distribute-money-to-maximum-children/description/

class Solution:
    def distMoney(self, money: int, children: int) -> int:
        """
        Logic: Brute Force (Greedy-implied)

        Time: O(money) --> O(max(200)) --> O(1)
        Space: O(1)
        """
        # Base cases
        if money < children:
            return -1
        if money == (8*children): 
            return children
        if money > (8*children):
            return children-1

        # Get as much children with 8 dollars as possible
        count = 0
        
        while money > 0 and money-8 >= children-1:
            count += 1
            money -= 8
            children -= 1
        
        # If any children left with 4, take away one child 
        # from `count` to share
        if money == 4 and children == 1:
            count -= 1

        return count
