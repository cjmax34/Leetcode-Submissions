class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            'I': 1, 
            'IV':4, 
            'V': 5, 
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000
            }
        n = len(s) - 1
        sum = 0

        while n >= 0:
            if ((s[n] == 'D' or s[n] == 'M') and s[n-1] == 'C' and n-1 >= 0) or ((s[n] == 'L' or s[n] == 'C') and s[n-1] == 'X' and n-1 >= 0) or ((s[n] == 'V' or s[n] == 'X') and s[n-1] == 'I' and n-1 >= 0):
                sum += values[s[n-1] + s[n]]
                n -= 2
            else:
                sum += values[s[n]]
                n -= 1

        return sum