class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        """
        Logic: Straightforward Boolean Flags
        
        Time: O(n)
        Space: O(1)
        """
        is_8_c = is_1_low = is_1_up = is_1_d = is_1_sp = False
        has_adj_c = False
        n = len(password)
        
        for i in range(len(password)):
            if n >= 8: is_8_c = True
            if password[i].islower(): is_1_low = True
            if password[i].isupper(): is_1_up = True
            if password[i].isdigit(): is_1_d = True
            if password[i] in "!@#$%^&*()-+": is_1_sp = True
        
        for i in range(1, len(password)):
            if password[i-1] == password[i]:
                return False
        
        return (is_8_c and is_1_low and is_1_up \
                and is_1_d and is_1_sp and not has_adj_c)
