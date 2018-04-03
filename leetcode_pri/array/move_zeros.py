# coding=utf-8
"""
给定一个数组 nums, 编写一个函数将所有 0 移动到它的末尾，同时保持非零元素的相对顺序。

例如， 定义 nums = [0, 1, 0, 3, 12]，调用函数之后， nums 应为 [1, 3, 12, 0, 0]。

注意事项:

必须在原数组上操作，不要为一个新数组分配额外空间。
尽量减少操作总数。
"""


def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    i = 0  # 记录不为0的数的下标
    for j in range(len(nums)):
       if nums[j] == 0:
           continue
       else:
           nums[i] = nums[j]
           i += 1
    for k in range(i, len(nums)):
        nums[k] = 0


if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    moveZeroes(nums)
    print(nums)