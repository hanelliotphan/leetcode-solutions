class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Logic: Reverse the `digits` list, if the current digit is a 9,
                update `carry` to increment the next digit later 
                via `i` index.
                If `i` exceeds the length of `digits`, append `1` to digits.
                Then, reverse `digits` back to original state and return.
                
        Time: O(n)
        Space: O(1)
        """
        digits = digits[::-1]
        carry, i = 1, 0
        
        while carry:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    carry = 0
            else:
                digits.append(1)
                carry = 0
            i += 1
        
        return digits[::-1]
