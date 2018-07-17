# coding=utf-8
"""
给定一个Excel表格中的列名称，返回其相应的列序号。

例如，

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
示例 1:

输入: "A"
输出: 1
示例 2:

输入: "AB"
输出: 28
示例 3:

输入: "ZY"
输出: 701
"""
def titleToNumber(s):
    """
    :type s: str
    :rtype: int
    """
    # ord() 字符转整数  chr() 整数转字符
    # 1.生成字母表
    dict = {}
    for i in range(26):
        dict[chr(ord('A') + i)] = i + 1
    res = 0
    weight = 1
    for i in range(len(s)):
        c = s[len(s) - 1 - i]
        res += dict[c] * weight
        weight *= 26
    return res


if __name__ == '__main__':
    print(titleToNumber("ZY"))