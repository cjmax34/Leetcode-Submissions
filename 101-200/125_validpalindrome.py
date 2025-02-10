def isPalindrome(s):
    s = s.replace(' ', '')
    s = ''.join(filter(str.isalnum, s)).lower()
    
    return s == s[::-1]

print(isPalindrome("race car"))