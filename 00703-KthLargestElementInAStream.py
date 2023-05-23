# https://leetcode.com/problems/kth-largest-element-in-a-stream/description/

class KthLargest:
    """
    Logic: Sort
    
    Time: O(n*logn)
    Space: O(1)
    """
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort(reverse=True)
        return self.nums[self.k-1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
