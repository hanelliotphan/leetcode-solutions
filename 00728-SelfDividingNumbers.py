class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        """
        Logic: Digit Modulo
        
        Time: O(n)
        Space: O(1)
        """
        def is_self_diving(n):
            tmp = n
            while tmp > 0:
                d = tmp % 10
                if d == 0:
                    return False
                elif d != 0 and n % d != 0:
                    return False
                tmp = tmp // 10
            return True
        
        res = []
        
        for n in range(left, right+1):
            if is_self_diving(n):
                res.append(n)
                
        return res
