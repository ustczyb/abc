# coding=utf-8
"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
"""
def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    dict = {
        ')':'(',
        ']':'[',
        '}':'{'
    }
    for c in s:
        if c in ['(', '[', '{']:
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            if not dict[c] == stack.pop():
                return False
    return len(stack) == 0
