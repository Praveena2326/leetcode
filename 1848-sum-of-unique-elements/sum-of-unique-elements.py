class Solution(object):
    def sumOfUnique(self, nums):
       temp=[]
       duplicate=[]

       for x in nums:
            if x in temp:
                temp.remove(x)
                duplicate.append(x)
            elif x not in duplicate:
                temp.append(x)
       return sum(temp)
            