# coding=utf-8
"""
给定一个序列（至少含有 1 个数），从该序列中寻找一个连续的子序列，使得子序列的和最大。

例如，给定序列 [-2,1,-3,4,-1,2,1,-5,4]，
连续子序列 [4,-1,2,1] 的和最大，为 6。

扩展练习:

若你已实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
"""


def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    if n == 0:
        return 0
    tmp = n * [0]
    tmp[0] = nums[0]
    for i in range(1, n):
        if tmp[i - 1] >= 0:
            tmp[i] = tmp[i - 1] + nums[i]
        else:
            tmp[i] = nums[i]
    return max(tmp)


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(maxSubArray(nums))
