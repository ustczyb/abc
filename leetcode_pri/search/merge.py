# coding=utf-8
"""
给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1中，使得 num1 成为一个有序数组。

注意:

你可以假设 nums1有足够的空间（空间大小大于或等于m + n）来保存 nums2 中的元素。在 nums1 和 nums2 中初始化的元素的数量分别是 m 和 n。
"""


def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    if m == 0:
        for i in range(n):
            nums1[i] = nums2[i]
        return
    if n == 0:
        return
    nums = (m + n) * [0]
    i = j = k = 0
    while i < m or j < n:
        if i < m and (j == n or nums1[i] <= nums2[j]):
            nums[k] = nums1[i]
            k += 1
            i += 1
        elif j < n and (i == m or nums1[i] > nums2[j]):
            nums[k] = nums2[j]
            k += 1
            j += 1
    for i in range(m + n):
        nums1[i] = nums[i]


# leetcode上的优雅解答
# def merge(nums1, m, nums2, n):
#     while m>0 and n>0:
#         if nums1[m-1] > nums2[n-1]:
#             nums1[m+n-1] = nums1[m-1]
#             m = m-1
#         else:
#             nums1[m+n-1] = nums2[n-1]
#             n = n-1
#     if n > 0:
#         nums1[:n] = nums2[:n]

if __name__ == '__main__':
    nums1 = [1, 0]
    nums2 = [2]
    merge(nums1, 1, nums2, 1)
    print(nums1)
