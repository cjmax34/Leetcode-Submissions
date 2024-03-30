def productExceptSelf(nums):
    products = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        products[i] *= prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(len(nums) - 1, -1, -1):
        products[i] *= suffix
        suffix *= nums[i]

    return products

print(productExceptSelf([1,2,3,4]))
