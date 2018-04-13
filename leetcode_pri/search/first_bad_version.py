# coding=utf-8
"""
你是产品经理，目前正在领导一个团队开发一个新产品。不幸的是，您的产品的最新版本没有通过质量检查。由于每个版本都是基于之前的版本开发的，所以错误版本之后的所有版本都是不好的。

假设你有 n 个版本 [1, 2, ..., n]，你想找出第一个错误的版本，导致下面所有的错误。

你可以通过 bool isBadVersion(version) 的接口来判断版本号 version 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。您应该尽量减少对 API 的调用次数。
"""


def firstBadVersion(n):
    """
    :type n: int
    :rtype: int
    """
    low = 1
    high = n
    while low <= high:
        if isBadVersion(low):
            return low
        if not isBadVersion(high):
            return high + 1

        mid = (low + high) / 2
        if isBadVersion(mid):
            high = mid - 1
        else:
            low = mid + 1
    return low


def isBadVersion(v):
    if v >= 2:
        return True
    return False


if __name__ == '__main__':
    print(firstBadVersion(3))