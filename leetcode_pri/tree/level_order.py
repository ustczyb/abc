# coding=utf-8
"""
给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
"""
from leetcode_pri.tree.TreeNode import TreeNode


def levelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    res = []
    if not root:
        return res
    layer = []
    layer.append(root)
    while(len(layer) > 0):
        l = []
        for i in layer:
            l.append(i.val)
        res.append(l)
        n = len(layer)
        for i in range(n):
            p = layer.pop(0)
            if p.left:
                layer.append(p.left)
            if p.right:
                layer.append(p.right)
    return res

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
    print(levelOrder(t1))