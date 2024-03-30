def topKFrequent(nums, k):
    num_hash = {}

    for n in nums:
        if n not in num_hash:
            num_hash[n] = 0
        num_hash[n] += 1
    
    num_hash = dict(sorted(num_hash.items(), key=lambda x:x[1], reverse=True))
    
    res = []

    for i in range(k):
        res.append(list(num_hash.keys())[i])
    
    return res

topKFrequent([2, 2, 3, 3, 4, 1, 1, 1], 2)