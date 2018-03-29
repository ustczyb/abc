# coding=utf-8
"""
计算所有小于非负数整数 n 的质数数量
"""

from math import sqrt


def count_primes(n):
    """
    :type n: int
    :rtype: int
    """
    if n < 2:
        return 0
    tmp = n * [1]
    for i in range(2, int(sqrt(n)) + 1):
        for j in range(2 * i - 1, len(tmp), i):
            tmp[j] = 0
    res = 0
    for i in tmp:
        res += i
    return res - 1
 

if __name__ == '__main__':
    print(count_primes(2))
