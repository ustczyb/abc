"""
给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。

示例 1:

输入:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
示例 2:

输入:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
输出:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
进阶:

一个直接的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
你能想出一个常数空间的解决方案吗？

空间占用O(1)的最优解：
按从左到右从上到下的顺序找到原始数据中第一个0元素（其实可以是任意一个0元素），假设为X[row][col]，则用X中的第row行和第col列空间来作为标记空间。其中第row行用来标记某一列是否需要置零，第col列用来标记某一行是否需要置零
遍历原始数据，如果某一元素为X[i][j]=0，则修改X[row][j]和X[i][col]
根据第row行和第col列，对X中的元素进行置零
"""


def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    # 1.选出所有的0所在的行与列
    row_zero = set()
    col_zero = set()
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                row_zero.add(i)
                col_zero.add(j)
    # 2.将这些行与列上的元素置为0
    for i in row_zero:
        for j in range(n):
            matrix[i][j] = 0
    for j in col_zero:
        for i in range(m):
            matrix[i][j] = 0


if __name__ == '__main__':
    matrix = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    setZeroes(matrix)
    print(matrix)
