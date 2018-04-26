# coding=utf-8
"""
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:

输入:
    2
   / \
  1   3
输出: true
示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。
"""
from leetcode_pri.tree.TreeNode import TreeNode


def isValidBST(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    list = []
    def tree_to_list(root):
        if not root:
            return
        tree_to_list(root.left)
        list.append(root.val)
        tree_to_list(root.right)
    tree_to_list(root)
    for i in range(len(list) - 1):
        if list[i] >= list[i + 1]:
            return False
    return True



if __name__ == '__main__':
    t1 = TreeNode(1)
    t2 = TreeNode(1)
    t1.right = t2
    print(isValidBST(t1))