# coding=utf-8
"""
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
说明:

如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
"""
from leetcode_pri.tree.TreeNode import TreeNode


def is_symmetric(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if not root:
        return True
    layer = []
    layer.append(root)
    while len(layer) > 0:
        n = len(layer)
        for i in range(n / 2):
            if not layer[i] and not layer[n - 1 - i]:
                continue
            if not (layer[i] and layer[n - 1 - i]):
                return False
            if not layer[i].val == layer[n - 1 - i].val:
                return False
        for i in range(n):
            p = layer.pop(0)
            if p:
                layer.append(p.left)
                layer.append(p.right)
    return True


if __name__ == '__main__':
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(2)
    t4 = TreeNode(3)
    t5 = TreeNode(3)
    t1.left = t2
    t1.right = t3
    t2.right = t4
    t3.right = t5
    print(is_symmetric(t1))