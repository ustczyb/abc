# coding=utf-8
"""
数数并说序列是一个整数序列，第二项起每一项的值为对前一项的计数，其前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作 "一个一" 即 11。
11 被读作  "两个一" 即 21。
21 被读作  "一个二 和 一个一" 即 1211。

给一个正整数 n ，输出数数并说序列的第 n 项。

注意：该整数序列的每项都输出为字符串。

例 1:

输入: 1
输出: "1"

例 2:
输入: 4
输出: "1211"
"""


def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """
    arr = n * ['1']
    for i in range(1, n):
        last = arr[i - 1]
        arr[i] = single_count(last)
    return arr[n - 1]


def single_count(s):
    n = len(s)
    i = 0
    res = ''
    count = 0
    while i < n:
        count += 1
        if  i == n - 1 or s[i] != s[i + 1]:
            res += str(count) + s[i]
            count = 0
        i += 1
    return res


if __name__ == '__main__':
    s = '21'
    print(countAndSay(5))
