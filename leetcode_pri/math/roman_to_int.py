# coding=utf-8
"""
给定一个罗马数字，将其转换成整数。
Ⅰ（1）、Ⅴ（5）、Ⅹ（10）、Ⅼ（50）、Ⅽ（100）、Ⅾ（500）和Ⅿ（1000）
返回的结果要求在 1 到 3999 的范围内。
"""


def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    vocab_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C':100,
        'D':500,
        'M':1000
    }
    res = 0
    for i in range(len(s)):
        v = vocab_map[s[i]]
        if i == len(s) - 1 or vocab_map[s[i + 1]] <= v:
            res += v
        else:
            res -= v
    return res


if __name__ == '__main__':
    print(romanToInt("MCMXCIV"))
