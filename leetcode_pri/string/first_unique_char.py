# coding=utf-8
"""
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

案例:

s = "leetcode"
返回 0.

s = "loveleetcode",
返回 2.


注意事项：您可以假定该字符串只包含小写字母。
"""


def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """
    s_list = list(s)
    tmp = {}
    i = 0
    for c in s_list:
        if tmp.get(c) == None:
            tmp[c] = i
            i += 1
        else:
            tmp[c] = -1
    res = -1
    min = len(s)
    for t in tmp.items():
        if t[1] >= 0 and t[1] < min:
            min = t[1]
            res = s_list.index(t[0])
    return res


if __name__ == '__main__':
    s = "loveleetcode"
    print(firstUniqChar(s))
