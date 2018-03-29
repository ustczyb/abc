# coding=utf-8
"""
给定一个罗马数字，将其转换成整数。
Ⅰ（1）、Ⅴ（5）、Ⅹ（10）、Ⅼ（50）、Ⅽ（100）、Ⅾ（500）和Ⅿ（1000）
返回的结果要求在 1 到 3999 的范围内。
"""
def romanToInt(self, s):
    """
    :type s: str
    :rtype: int
    """
    vocab_list = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
