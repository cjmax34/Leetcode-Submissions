class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_words = s.split(" ")
        if len(pattern) != len(s_words):
            return False

        hashh = {}

        for char, word in zip(pattern, s_words):
            if char in hashh:
                if hashh[char] != word:
                    return False
            elif word in hashh.values():
                return False

            hashh[char] = word

        return True