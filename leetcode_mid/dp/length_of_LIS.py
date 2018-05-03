# coding=utf-8
"""
给出一个无序的整形数组，找到最长上升子序列的长度。

例如，

给出 [10, 9, 2, 5, 3, 7, 101, 18]，
最长的上升子序列是 [2, 3, 7, 101]，因此它的长度是4。因为可能会有超过一种的最长上升子序列的组合，因此你只需要输出对应的长度即可。

你的算法的时间复杂度应该在 O(n2) 之内。

进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
"""


def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    # 解法1:对数组排序，求排序后的数组和原数组的最长公共子序列 复杂度为O(n ^ 2) 会超时
    # A[m + 1, n + 1] = A[m, n] + 1  (if num1[numsm + 1] == num2[n + 1])
    #                 = max{A[m, n + 1], A[m + 1, n]}
    # 排序后的数组去重
    # sort_nums = sorted(nums)
    # s_nums = list(set(sort_nums))
    # s_nums.sort(key=sort_nums.index)
    # n = len(nums)
    # m = len(s_nums)
    # res = []
    # for i in range(n + 1):
    #     l = (m + 1) * [0]
    #     res.append(l)
    # for i in range(1, n + 1):
    #     for j in range(1, m + 1):
    #         if nums[i - 1] == s_nums[j - 1]:
    #             res[i][j] = res[i - 1][j - 1] + 1
    #         else:
    #             res[i][j] = max(res[i][j - 1], res[i - 1][j])
    # return res[n][m]
    # 解法二:d[k]表示长为k的递增子序列的最小末位数字
    def binary_search(nums, k, low, high):
        if low >= high:
            if nums[low] >= k:
                return low
            else:
                return low + 1
        mid = (low + high) / 2
        if nums[mid] == k:
            return mid
        elif nums[mid] > k:
            return binary_search(nums, k, low, mid - 1)
        elif nums[mid] < k:
            return binary_search(nums, k, mid + 1, high)

    d = []
    for i in range(len(nums)):
        n = len(d)
        l = nums[i]
        if n == 0 or d[n - 1] < l:
            d.append(l)
        else:
            ind = binary_search(d, l, 0, n - 1)
            d[ind] = l
    return len(d)


if __name__ == '__main__':
    nums = [2, 2]
    print(lengthOfLIS(nums))
