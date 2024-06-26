def reverseVowels(s):
    start, end = 0, len(s) - 1
    s = list(s)
    vowels = 'aeiouAEIOU'

    while start < end:
        if s[start] in vowels and s[end] in vowels:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        elif s[end] not in vowels:
            end -= 1
        elif s[start] not in vowels:
            start += 1

    return ''.join(s)