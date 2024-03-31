# def moveZeroes(nums):
#     non_zero = []
#     zeroes = []

#     for i in nums:
#         if i == 0:
#             zeroes.append(i)
#         else:
#             non_zero.append(i)

#     print(non_zero+zeroes)

def moveZeroes(nums):
    left_ptr = 0
    right_ptr = 0

    for _ in nums:
        if nums[right_ptr] != 0:
            nums[left_ptr], nums[right_ptr] = nums[right_ptr], nums[left_ptr]
            left_ptr += 1
            right_ptr += 1
        else:
            right_ptr += 1