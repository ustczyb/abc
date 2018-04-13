def deleteNode(node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    if node.next == None:
        node = None
        return
    v = node.next.val
    node.next = node.next.next
    node.val = v
