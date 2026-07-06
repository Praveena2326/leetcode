class Solution(object):
    def minSubArrayLen(self, target, nums):
        left=0
        right=0
        minimum=[] #assume any value or apply minimum=[]
        subarray=0
        while right < len(nums):
            subarray+= nums[right]
            while subarray>=target:
                minimum.append(right-left+1)
                subarray -= nums[left]
                left +=1
            right +=1
        return 0 if len(minimum)==0 else min(minimum)
