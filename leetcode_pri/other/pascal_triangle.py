# coding=utf-8
"""
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。

在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    if numRows == 0:
        return []
    if numRows == 1:
        return [[1]]
    res = [[1]]
    for i in range(1, numRows):
        last_row = res[i - 1]
        cur_row = []
        cur_row.append(1)
        for j in range(i - 1):
            cur_row.append(last_row[j] + last_row[j + 1])
        cur_row.append(1)
        res.append(cur_row)
    return res


if __name__ == '__main__':
    print(generate(5))
