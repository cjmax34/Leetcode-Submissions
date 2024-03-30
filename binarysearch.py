def binarySearch(nums, target):
    left = 0
    right = len(nums)

    while (left < right):
        mid = (left+right)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    return -1

print(binarySearch([-1,0,3,5,9,12], 9))


