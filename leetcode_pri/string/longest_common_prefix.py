# coding=utf-8
"""
编写一个函数来查找字符串数组中的最长公共前缀
"""
def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if len(strs) == 0:
        return ''
    longest_prefix = ''
    first_str = strs[0]
    for i in range(len(first_str)):
        for k in range(1, len(strs)):
            if i >= len(strs[k]) or strs[k][i] != first_str[i]:
                return longest_prefix
        longest_prefix += first_str[i]
    return longest_prefix