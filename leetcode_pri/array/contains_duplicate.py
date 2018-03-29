# coding=utf-8
"""
给定一个整数数组，判断是否存在重复元素。

如果任何值在数组中出现至少两次，函数应该返回 true。如果每个元素都不相同，则返回 false。
"""


def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    s = set(nums)
    return len(s) != len(nums)


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(containsDuplicate(nums))
