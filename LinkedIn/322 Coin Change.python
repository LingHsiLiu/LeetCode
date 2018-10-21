# LeetCode 322 Coin Change
# You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# Example 1:

# Input: coins = [1, 2, 5], amount = 11
# Output: 3 
# Explanation: 11 = 5 + 5 + 1
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1
# Note:
# You may assume that you have an infinite number of each kind of coin.


class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort(reverse = True)
        # print(coins)
        lenc, self.res = len(coins), 2**31-1
        # print(self.res)

        def dfs(pt, rem, count):
            if not rem:
                self.res = min(self.res, count)
            for i in range(pt, lenc): #0, 3
                if coins[i] <= rem < coins[i] * (self.res-count): # if hope still exists
                    print(rem)
                    # print(coins[i])
                    dfs(i, rem-coins[i], count+1)
        for i in range(lenc):
            dfs(i, amount, 0)
        return self.res if self.res < 2**31-1 else -1
