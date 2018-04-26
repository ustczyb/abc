# coding=utf-8
"""
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定有序数组: [-10,-3,0,5,9],

一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5
"""
from leetcode_pri.tree.TreeNode import TreeNode


def sortedArrayToBST(nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    def array_to_BST(nums, begin, end):
        if begin > end:
            return None
        if begin == end:
            return TreeNode(nums[begin])
        mid = (begin + end) / 2
        root = TreeNode(nums[mid])
        root.left = array_to_BST(nums, begin, mid - 1)
        root.right = array_to_BST(nums, mid + 1, end)
        return root
    return array_to_BST(nums, 0, len(nums) - 1)