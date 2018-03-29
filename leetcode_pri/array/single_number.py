# coding=utf-8
"""
给定一个整数数组，除了某个元素外其余元素均出现两次。请找出这个只出现一次的元素。

备注：

你的算法应该是一个线性时间复杂度。 你可以不用额外空间来实现它吗？
"""


def single_number(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 1:
        return nums[0]
    res = nums[0]
    for i in range(1, len(nums)):
        res = res ^ nums[i]
    return res


if __name__ == '__main__':
    nums = [1, 2, 3, 3, 1]
    print(single_number(nums))
