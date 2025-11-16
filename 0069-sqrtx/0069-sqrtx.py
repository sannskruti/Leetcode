class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        l = 1
        r = x

        while l <= r:
            mid = (r - l) // 2 + l  # integer midpoint

            if mid * mid > x:
                r = mid - 1
            elif mid * mid < x:
                l = mid + 1
            else:
                return mid

        return r