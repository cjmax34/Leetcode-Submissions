from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_counter = Counter(ransomNote)
        mag_counter = Counter(magazine)

        return (ransom_counter - mag_counter) == {}