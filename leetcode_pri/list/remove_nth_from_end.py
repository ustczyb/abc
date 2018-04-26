# coding=utf-8
"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？
"""
def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    first = head.next
    target = head
    if head.next == None:
        return None
    if n == 1:
        while not first.next == None:
            first = first.next
            target = target.next
        target.next = None
        return head
    for i in range(n - 1):
        first = first.next
    while not first == None:
        first = first.next
        target = target.next
    v = target.next.val
    target.next = target.next.next
    target.val = v
    return head


# leetcode上的更好的解答，加入头结点
# dummy = ListNode(0)
# dummy.next = head
# p1 = p2 = dummy
# for i in range(n):
#     p1 = p1.next
# while p1.next:
#     p1 = p1.next
#     p2 = p2.next
# p2.next = p2.next.next
# return dummy.next