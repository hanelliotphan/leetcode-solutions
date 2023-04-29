# https://leetcode.com/problems/three-divisors/description/

class Solution:
    def isThree(self, n: int) -> bool:
        """
        Logic: Prime Factors
        
        Time: O(1)
        Space: O(1)
        """
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 
                23, 29, 31, 37, 41, 43, 47, 
                53, 59, 61, 67, 71, 73, 79, 
                83, 89, 97]
        
        return sqrt(n) in primes
