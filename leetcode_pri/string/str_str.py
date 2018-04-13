# coding=utf-8
"""
返回蕴含在 haystack 中的 needle 的第一个字符的索引，如果 needle 不是 haystack 的一部分则返回 -1 。

例 1:

输入: haystack = "hello", needle = "ll"
输出: 2

例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1
"""
def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    return haystack.find(needle)


if __name__ == '__main__':
    haystack = "hello"
    needle = "ll"
    print(strStr(haystack, needle))