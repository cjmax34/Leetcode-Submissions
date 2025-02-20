def maxVowels(s, k):
    curr = res = 0
    
    for i in range(len(s)):
        if i >= k and s[i-k] in ('a','e','i','o','u'):
            curr -= 1
        if s[i] in ('a','e','i','o','u'):
            curr += 1
        res = max(res, curr)

    return res