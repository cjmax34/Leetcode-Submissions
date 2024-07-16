class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        length = 0

        while (i >= 0):
            if s[i] != " ":
                length += 1
            elif s[i] == " " and length > 0:
                break
            i -= 1

        return length