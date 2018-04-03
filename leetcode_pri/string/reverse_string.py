# coding=utf-8
"""
请编写一个函数，其功能是将输入的字符串反转过来。

示例：

输入：s = "hello"
返回："olleh"
"""


def reverseString(s):
    """
    :type s: str
    :rtype: str
    """
    l = list(s)
    l.reverse()
    return "".join(l)


if __name__ == '__main__':
    s = "hello"
    print(reverseString(s))
