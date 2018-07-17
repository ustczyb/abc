"""
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：

所有输入均为小写字母。
不考虑答案输出的顺序。

"""


def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    dict = {}
    res = []
    for s in strs:
        compared_list = list(s)
        compared_list.sort()
        compared_str = str(compared_list)
        if not dict.get(compared_str):
            dict[compared_str] = []
        dict[compared_str].append(s)
    for d in dict:
        res.append(dict[d])
    return res


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(groupAnagrams(strs))