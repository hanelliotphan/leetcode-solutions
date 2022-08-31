class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        """
        Logic: Hash Map
        
        Time: O(n)
        Space: O(n)
        """
        ball_box_map = dict()
        
        for ball in range(lowLimit, highLimit+1):
            digits = []
            while ball > 0:
                digits.append(ball % 10)
                ball //= 10
            box = sum(digits)
            if box not in ball_box_map:
                ball_box_map[box] = 1
            else:
                ball_box_map[box] += 1
                
        return max(ball_box_map.values())
