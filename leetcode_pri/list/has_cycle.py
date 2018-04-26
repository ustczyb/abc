# coding=utf-8
"""
给定一个链表，判断链表中是否有环。

进阶：
你能否不使用额外空间解决此题？
"""


def hasCycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    if head == None or head.next == None:
        return False
    p1 = head
    p2 = head.next.next
    while (p2 != None and p2.next != None):
        if p1 == p2:
           return True
        p1 = p1.next
        p2 = p2.next.next
    return False

# leetcode好的解答
# while head:
#     if head.val is TAG:
#         return True
#     head.val = TAG
#     head = head.next
# return False