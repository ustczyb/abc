# coding=utf-8
"""
编写一个函数，输入是一个无符号整数，返回的是它所有 位1 的个数（也被称为汉明重量）。

例如，32位整数 '11' 的二进制表示为 00000000000000000000000000001011，所以函数返回3。
"""
def hammingWeight(n):
    """
    :type n: int
    :rtype: int
    """
    count = 0
    while n > 0:
        if n % 2 == 1:
            count += 1
        n /= 2
    return count