class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []

        for op in operations:
            if op == "C":
                stk.pop()
            elif op == "D":
                stk.append(stk[-1]*2)
            elif op == "+":
                stk.append(stk[-2]+stk[-1])
            else:
                stk.append(int(op))
            print(stk)
        
        return sum(stk)