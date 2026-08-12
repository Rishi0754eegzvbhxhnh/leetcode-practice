class Solution:
    def maximumWealth(self, accounts):
        max_wealth = 0
        for customer in accounts:
            wealth = sum(customer)   # sum of one customer's accounts
            if wealth > max_wealth:
                max_wealth = wealth
        return max_wealth