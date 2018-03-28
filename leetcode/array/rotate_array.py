# coding=utf-8
"""
将包含 n 个元素的数组向右旋转 k 步。

例如，如果  n = 7 ,  k = 3，给定数组  [1,2,3,4,5,6,7]  ，向右旋转后的结果为 [5,6,7,1,2,3,4]。

注意:

尽可能找到更多的解决方案，这里最少有三种不同的方法解决这个问题。
"""


def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    nums[:] = nums[n - k:] + nums[:n - k]


# 翻转[i, j-1]
def reverse(nums, i, j):
    for k in range(i, (i + j - 1) / 2 + 1):
        swap(nums, k, i + j - k - 1)


def swap(nums, i, j):
    tmp = nums[i]
    nums[i] = nums[j]
    nums[j] = tmp


if __name__ == '__main__':
    nums = range(1, 7)
    rotate(nums, 3)
    print(nums)
