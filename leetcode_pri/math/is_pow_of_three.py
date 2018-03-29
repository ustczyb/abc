# coding=utf-8
"""
给出一个整数，写一个函数来确定这个数是不是3的一个幂。

后续挑战：
你能不使用循环或者递归完成本题吗？
"""
def isPowerOfThree(n):
    """
    :type n: int
    :rtype: bool
    """
    # 方法1：递归
    # if n == 0:
    #     return False
    # if n == 1:
    #     return True
    # if n % 3 != 0:
    #     return False
    # return isPowerOfThree(n / 3)

    if n == 0:
        return False
    while n % 3 == 0:
        n = n / 3
    if n == 1:
        return True
    return False


if __name__ == '__main__':
    print(isPowerOfThree(82))