def reverseWords(s):
    reversed = " ".join(word[::-1] for word in s.split(" "))
    return reversed
    
print(reverseWords("Let's take LeetCode contest"))