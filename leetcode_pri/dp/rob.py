# coding=utf-8
"""
你是一个专业的强盗，计划抢劫沿街的房屋。每间房都藏有一定的现金，阻止你抢劫他们的唯一的制约因素就是相邻的房屋有保安系统连接，如果两间相邻的房屋在同一晚上被闯入，它会自动联系警方。

给定一个代表每个房屋的金额的非负整数列表，确定你可以在没有提醒警方的情况下抢劫的最高金额。
"""
def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0], nums[1])
    tmp = (n + 1) * [0]
    tmp[0] = 0
    tmp[1] = nums[0]
    tmp[2] = nums[1]
    for i in range(3, n + 1):
        tmp[i] = max(tmp[i - 2], tmp[i - 3]) + nums[i - 1]
    return max(tmp)


