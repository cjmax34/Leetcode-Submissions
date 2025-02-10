# def strStr(haystack, needle):
#     return haystack.find(needle)

def strStr(haystack, needle):
    for i in range(len(haystack)):
        if haystack[i: i+len(needle)] == needle:
            return i    # Success
    return -1   # Fail