from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        text_count = Counter(text)
        
        return min(text_count['b'], text_count['a'], text_count['l']//2, text_count['o']//2, text_count['n'])