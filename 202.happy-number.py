class Solution:
    def isHappy(self, n: int) -> bool:
        n = str(n)
        seen = set()

        while n not in seen:
            seen.add(n)

            sum = 0
            for num in n:
                sum += int(num) ** 2

            if sum == 1:
                return True

            n = str(sum)