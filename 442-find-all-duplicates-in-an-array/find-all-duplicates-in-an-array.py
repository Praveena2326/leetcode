class Solution:
    def findDuplicates(self, nums):
        seen = set()
        ans = []

        for num in nums:
            if num in seen:
                ans.append(num)
            else:
                seen.add(num)

        return ans