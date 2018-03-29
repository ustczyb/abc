# coding=utf-8
"""
给定一个有序数组，你需要原地删除其中的重复内容，使每个元素只出现一次,并返回新的长度。

不要另外定义一个数组，您必须通过用 O(1) 额外内存原地修改输入的数组来做到这一点。

示例：

给定数组: nums = [1,1,2],

你的函数应该返回新长度 2, 并且原数组nums的前两个元素必须是1和2
不需要理会新的数组长度后面的元素
"""


def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return 0
    res = 1
    for i in range(1, len(nums)):
        if nums[res - 1] < nums[i]:
            nums[res] = nums[i]
            res += 1
    return res


if __name__ == '__main__':
    nums = [1, 1, 2]
    res = removeDuplicates(nums)
    print(res)
    print(nums)
