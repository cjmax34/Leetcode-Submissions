def maxNumberOfBalloons(text):
    hash_tbl = Counter(text)

    return min(hash_tbl['b'], hash_tbl['a'], hash_tbl['l']//2, hash_tbl['o']//2, hash_tbl['n'])