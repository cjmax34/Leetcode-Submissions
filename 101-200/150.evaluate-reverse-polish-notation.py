class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        
        for token in tokens:
            if token in "+-*/":
                a, b = stk.pop(), stk.pop()            
                if token == "+":
                    stk.append(b+a)
                elif token == "-":
                    stk.append(b-a)
                elif token == "*":
                    stk.append(b*a)
                elif token == "/":
                    stk.append(int(b/a))
            else:
                stk.append(int(token))

        return stk[-1]