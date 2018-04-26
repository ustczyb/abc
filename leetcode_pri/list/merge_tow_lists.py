# coding=utf-8
"""
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""
from leetcode_pri.list.list_node import ListNode


def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    h = ListNode(0)
    p = h
    while not l1 == None and not l2 == None:
        if l1.val < l2.val:
            p.next = l1
            p = p.next
            l1 = l1.next
        else:
            p.next = l2
            p = p.next
            l2 = l2.next
    if not l1 == None:
        p.next = l1
    else:
        p.next = l2
    return h.next