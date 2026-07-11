class Solution:
    def minSwaps(self, nums):
        n = len(nums)
        ones = sum(nums)

        if ones == 0 or ones == n:
            return 0

        curr = sum(nums[:ones])
        max_ones = curr

        for i in range(ones, n + ones):
            curr += nums[i % n]
            curr -= nums[(i - ones) % n]
            max_ones = max(max_ones, curr)

        return ones - max_ones