# coding=utf-8
"""
反转一个单链表。

进阶:
链表可以迭代或递归地反转。你能否两个都实现一遍？
"""
from leetcode_pri.list.list_node import ListNode


def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    def reverse_list(head):
        if head == None:
            return (None, None)
        if head.next == None:
            return (head, head)
        h, t = reverse_list(head.next)
        t.next = head
        head.next = None
        return h, head
    h, t = reverse_list(head)
    return h


# pre, cur = None, head
# while cur:
#     tmp = cur.next
#     cur.next = pre
#     pre = cur
#     cur = tmp
# return pre

if __name__ == '__main__':
    p1 = ListNode(1)
    p2 = ListNode(2)
    p1.next = p2
    p = reverseList(p1)
    print(p.val)