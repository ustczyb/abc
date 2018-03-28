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
    if len(nums) <= 1:
        return False
    res = nums[0]
    for i in range(1, len(nums)):
        res = res ^ nums[i]
    if res == 0:
        return True
    return False


if __name__ == '__main__':
    nums = [1,2,3,1]
    print()