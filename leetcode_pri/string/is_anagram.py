# coding=utf-8
"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。

例如，
s = "anagram"，t = "nagaram"，返回 true
s = "rat"，t = "car"，返回 false

注意:
假定字符串只包含小写字母。

提升难度:
输入的字符串包含 unicode 字符怎么办？你能能否调整你的解法来适应这种情况？
"""


def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if not len(s) == len(t):
        return False
    s_list = list(s)
    tmp_s = {}
    for c in s_list:
        if tmp_s.get(c) == None:
            tmp_s[c] = 1
        else:
            tmp_s[c] += 1
    for c in t:
        if tmp_s.get(c) == None:
            return False
        elif tmp_s.get(c) == 1:
            tmp_s.pop(c)
        else:
            tmp_s[c] -= 1
    return True

# 使用python api的简洁解答，时间复杂度应该是O(k * n)，k为不同的字符个数，因为每次count操作复杂度为O(n)
# def isAnagram(self, s, t):
#     """
#     :type s: str
#     :type t: str
#     :rtype: bool
#     """
#     if len(s) != len(t):
#         return False
#
#     d_char = {}
#     for char in s:
#         if not char in d_char:
#             if s.count(char) != t.count(char):
#                 return False
#             d_char[char] = 1
#     return True

if __name__ == '__main__':
    s = "rat"
    t = "car"
    print(isAnagram(s, t))