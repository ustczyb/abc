# coding=utf-8
"""
给定一个非负整数组成的非空数组，给整数加一。

可以假设整数不包含任何前导零，除了数字0本身。

最高位数字存放在列表的首位。
"""


def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    n = len(digits)
    res = n * [0]
    for i in range(n - 1, -1, -1):
        res[i] = digits[i] + 1
        if res[i] == 10:
            res[i] = 0
        else:
            break
    if i == 0 and res[i] == 0:
            res = (n + 1) * [0]
            res[0] = 1
            return res
    for j in range(i):
        res[j] = digits[j]
    return res


if __name__ == '__main__':
    num = [9,9]
    print(plusOne(num))