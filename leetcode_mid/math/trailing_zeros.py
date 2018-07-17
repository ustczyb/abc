# coding=utf-8
"""
给定一个整数 n，返回 n! 结果尾数中零的数量。

示例 1:

输入: 3
输出: 0
解释: 3! = 6, 尾数中没有零。
示例 2:

输入: 5
输出: 1
解释: 5! = 120, 尾数中有 1 个零.
说明: 你算法的时间复杂度应为 O(logN) 。
"""


def trailingZeroes(n):
    """
    :type n: int
    :rtype: int
    """
    k = 5
    res = 0
    while(n >= k):
        res += n / k
        k *= 5
    return res


if __name__ == '__main__':
    print(trailingZeroes(4))