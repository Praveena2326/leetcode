class Solution(object):
    def maximumWealth(self, accounts):
        richest=0
        for customers in accounts:
            wealth= sum(customers)
            if wealth>richest:
                richest= wealth
        return richest