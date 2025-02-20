class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num

        while left <= right:
            mid = (left+right)//2
            if mid*mid < num:
                left = mid+1
            elif mid*mid > num:
                right = mid-1
            else:
                return True

        return False