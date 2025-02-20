def mergeAlternately(word1, word2):
    res = ""
    max_len = max(len(word1), len(word2))

    for i in range(max_len):
        if i < len(word1) and i < len(word2):
            res += word1[i] + word2[i]
        elif i < len(word1):
            res += word1[i]
        else:
            res += word2[i]

    return res