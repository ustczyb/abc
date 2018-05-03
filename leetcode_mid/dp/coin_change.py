# coding=utf-8
"""
给定不同面额的硬币(coins)和一个总金额(amount)。写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合方式能组成总金额，返回-1。

示例 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

示例 2:
coins = [2], amount = 3
return -1.

注意:

你可以认为每种硬币的数量是无限的。
"""
def coinChange(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    dp = [0] * (amount + 1)
    for i in range(1, amount + 1):
        if i < min(coins):
            dp[i] = -1
        elif i in coins:
            dp[i] = 1
        else:
            res = -1
            for a in [i - x for x in coins]:
                if a < 0 or dp[a] == -1:
                    continue
                if res == -1 and dp[a] > 0 or dp[a] + 1 < res:
                    res = dp[a] + 1
            dp[i] = res
    return dp[amount]


if __name__ == '__main__':
    print(coinChange([2], 3))
