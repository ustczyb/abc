# coding=utf-8
"""
给定一个范围为 32 位 int 的整数，将其颠倒。

例 1:

输入: 123
输出:  321

例 2:

输入: -123
输出: -321

例 3:

输入: 120
输出: 21

注意:

假设我们的环境只能处理 32 位 int 范围内的整数。根据这个假设，如果颠倒后的结果超过这个范围，则返回 0。
"""


def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    flag = False
    if x < 0:
        flag = True
        x = -x
    num_list = []
    while x > 0:
        num_list.append(x % 10)
        x = x / 10
    for i in range(len(num_list) - 1, -1, -1):
        x += num_list[i] * pow(10, len(num_list) - 1 - i)
    if x > pow(2, 31) - 1 or x < -pow(2,31):
        return 0
    if flag:
        return -x
    return x


if __name__ == '__main__':
   x = 1534236469
   print(reverse(x))