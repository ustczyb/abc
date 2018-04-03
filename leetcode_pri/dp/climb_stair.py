# coding=utf-8
"""
你正在爬楼梯。需要 n 步你才能到达顶部。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方式可以爬到楼顶呢？

注意：给定 n 将是一个正整数。



示例 1：

输入： 2
输出： 2
说明： 有两种方法可以爬到顶端。

1.  1 步 + 1 步
2.  2 步
"""


def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 0:
        return 1
    if n == 1:
        return 1
    arr = (n + 1) * [1]
    for i in range(2, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]
    return arr[n]