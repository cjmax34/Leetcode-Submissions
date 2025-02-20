def reverseWords(s):
    return " ".join(s.split()[::-1])

print(reverseWords("a good   example"))