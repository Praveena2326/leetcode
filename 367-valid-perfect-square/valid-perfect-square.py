class Solution(object):
    def isPerfectSquare(self, num):
        left = 1
        right = num

        while left <= right:
            mid = (left + right) // 2
            square = mid * mid

            if square == num:
                return True
            elif square < num:
                left = mid + 1   # move right side
            else:
                right = mid - 1  # move left side

        return False