# https://leetcode.com/problems/design-browser-history/description/

class BrowserHistory:
    """
    Logic: Dynamic Array + Two Pointers

    Time: O(n)
    Space: O(1) --> required to return O(n) space, no extra space needed
    """
    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.curr_index = 0
        self.final_index = 0

    def visit(self, url: str) -> None:
        self.curr_index += 1
        if self.curr_index < len(self.stack):
            self.stack[self.curr_index] = url
        else:
            self.stack.append(url)
        self.final_index = self.curr_index

    def back(self, steps: int) -> str:
        self.curr_index = max(0, self.curr_index-steps)
        return self.stack[self.curr_index]

    def forward(self, steps: int) -> str:
        self.curr_index = min(self.final_index, self.curr_index+steps)
        return self.stack[self.curr_index]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
