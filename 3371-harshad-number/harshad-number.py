class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
       sum=0
       m=x
       while m>0:
            
            sum=sum+m%10
            m//=10
       if x % sum==0:
            return sum
       else:
            return -1 