# coding=utf-8
"""
给定一个字符串，确定它是否是回文，只考虑字母数字字符和忽略大小写。

例如：
"A man, a plan, a canal: Panama" 是回文字符串。
"race a car" 不是回文字符串。

注意:
你有考虑过这个字符串可能是空的吗？ 在面试中这是一个很好的问题。

针对此题目，我们将空字符串定义为有效的回文字符串。
"""
def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    n = len(s)
    if n == 0:
        return True
    begin = 0
    end = n - 1
    while begin < end:
        if not s[begin].isalnum():
            begin += 1
            continue
        if not s[end].isalnum():
            end -= 1
            continue
        if s[begin].lower() == s[end].lower():
            begin += 1
            end -= 1
        else:
            return False
    return True

# leetcode上的最快解答，使用了python的正则表达式
# import re
# class Solution(object):
#     def isPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         s=re.sub('[^a-zA-Zr\d]','',s).lower()
#         return s==s[::-1]


if __name__ == '__main__':
    s = "race a car"
    print(isPalindrome(s))
