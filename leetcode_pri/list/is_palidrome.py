# coding=utf-8
"""
请检查一个链表是否为回文链表。

进阶：
你能在 O(n) 的时间和 O(1) 的额外空间中做到吗？
可以从中间节点开始，翻转后面的链表
"""
from leetcode_pri.list.list_node import ListNode


def isPalindrome(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    if head == None or head.next == None:
        return True
    n = 0
    p = head
    while not p == None:
        n += 1
        p = p.next
    stack = []
    p = head
    for i in range(n / 2):
        stack.append(p.val)
        p = p.next
    if n % 2 == 1:
        p = p.next
    while not p == None:
        if not stack.pop() == p.val:
            return False
        p = p.next
    return True


if __name__ == '__main__':
    p1 = ListNode(1)
    p2 = ListNode(2)
    p3 = ListNode(1)
    p1.next = p2
    p2.next = p3
    print isPalindrome(p1)