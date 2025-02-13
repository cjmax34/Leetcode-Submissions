class MinStack:

    def __init__(self):
        self.stk = []
        self.currMinList = []
        
    def push(self, val: int) -> None:
        self.stk.append(val)
        currMin = val if not self.currMinList else min(self.currMinList[-1][1], val)
        self.currMinList.append((val, currMin))

    def pop(self) -> None:
        self.stk.pop()
        self.currMinList.pop()
        
    def top(self) -> int:
        return self.stk[-1]
        
    def getMin(self) -> int:
        return self.currMinList[-1][1]
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()