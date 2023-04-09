class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        """
        Logic: Brute Force

        Time: O(n*logn)
        Space: O(1) --> no extra space needed besides array to return
        """
        def is_prime(n):
            if n <= 1:
                return False
            for i in range(2, int(n**0.5)+1):
                if n % i == 0:
                    return False
            return True
        
        nums_in_diagonal = []
        i = 0
        j = len(nums[0])-1
        
        for num in nums:
            if is_prime(num[i]):
                nums_in_diagonal.append(num[i])
            if is_prime(num[j]):
                nums_in_diagonal.append(num[j])
            i += 1
            j -= 1
        
        return max(nums_in_diagonal) if nums_in_diagonal else 0
