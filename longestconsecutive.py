def longestConsecutive(nums):
    num_set = set(nums)
    longest = 0

    for i in nums:
        if (i - 1) not in num_set:
            length = 0
            while (i + length) in num_set:
                length += 1
            longest = max(longest, length)

    return longest

print(longestConsecutive([100, 1, 2, 3, 4, 200]))