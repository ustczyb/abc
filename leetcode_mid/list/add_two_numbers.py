# coding=utf-8
"""
给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""
from leetcode_pri.list.list_node import ListNode


def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    p1 = l1
    p2 = l2
    head = ListNode(0)
    p = head
    c = 0
    while p1 and p2:
        sum = p1.val + p2.val + c
        c = sum / 10
        r = ListNode(sum % 10)
        p.next = r
        p = r
        p1 = p1.next
        p2 = p2.next
    while p1:
        sum = p1.val + c
        r = ListNode(sum % 10)
        c = sum / 10
        p.next = r
        p = r
        p1 = p1.next
    while p2:
        sum = p2.val + c
        r = ListNode(sum % 10)
        c = sum / 10
        p.next = r
        p = r
        p2 = p2.next
    if not p1 and not p2 and c > 0:
        r = ListNode(c)
        p.next = r
        return head.next
    return head.next