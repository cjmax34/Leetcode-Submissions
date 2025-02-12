class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stk = []
        for i in range(n):
            while stk and temperatures[i] > temperatures[stk[-1]]:
                j = stk.pop()
                answer[j] = i-j
            stk.append(i)

        return answer