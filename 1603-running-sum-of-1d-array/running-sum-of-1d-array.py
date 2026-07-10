class Solution(object):
    def runningSum(self, nums):
        sum=[]
        total=0
        for i in range(len(nums)):
            total=total+nums[i]
            sum.append(total)
        return sum
        

            

        