def permute(nums):
    if len(nums) == 0:
        return []

    if len(nums) == 1:
        return [nums]

    all_perms = []

    for i in range(len(nums)):
        new_lst = nums[:i] + nums[i+1:]
        for j in permute(new_lst):
            all_perms.append([nums[i]]+j)
        
    return all_perms