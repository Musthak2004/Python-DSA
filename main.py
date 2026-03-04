class Solution(object):
    def mySqrt(self, x):
        low = 0
        high = x
        while low <= high:
            mid = (low + high) // 2
            if mid * mid <= x:
                return mid
            elif mid * mid < x:
                high = mid - 1
            else:
                low = mid + 1
        return mid // 3


x = 4
obj = Solution()
print(obj.mySqrt(x))