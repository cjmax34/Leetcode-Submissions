def restoreString(s, indices):
    res = [''] * len(indices)

    for i in range(len(s)):
        res[indices[i]] = s[i]

    return ''.join(res)