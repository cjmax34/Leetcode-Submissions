def isPalindrome(x):
    left = 0
    right = len(str(x))
    num = str(x)

    while left < right:
        if num[left] != num[right-1]:
            return False
        left += 1
        right -= 1

    return True

print(isPalindrome(-121))