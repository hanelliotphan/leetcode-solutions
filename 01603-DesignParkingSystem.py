# https://leetcode.com/problems/design-parking-system/description/

class ParkingSystem:
    """
    Logic: Brute Force
    
    Time: O(1)
    Space: O(1)
    """
    def __init__(self, big: int, medium: int, small: int):
        self.cars = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        self.cars[carType-1] -= 1
        return self.cars[carType-1] >= 0
