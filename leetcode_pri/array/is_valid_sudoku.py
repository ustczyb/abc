# coding=utf-8
"""
判断一个数独是否有效，根据：Sudoku Puzzles - The Rules。

数独部分填了数字，空的部分用 '.' 表示。

一个部分填充是有效的数独。

说明:
一个有效的数独（填了一部分的）不一定是可解的，只要已经填的数字是有效的即可。
"""


def isValidSudoku(board):

    """
    :type board: List[List[str]]
    :rtype: bool
    """

    def isLineValid(nums):
        tmp = 9 * [0]
        for num in nums:
            if num == '.':
                continue
            tmp[int(num) - 1] += 1
        for i in tmp:
            if i > 1:
                return False
        return True


    # 行判断
    for line in board:
        if not isLineValid(line):
            return False
    # 列判断
    for i in range(len(board)):
        list = []
        for j in range(len(board)):
            list.append(board[j][i])
        if not isLineValid(list):
            return False
    # 九宫格判断
    for k in [0, 3, 6]:
        for l in [0, 3, 6]:
            list = []
            for i in range(3):
                for j in range(3):
                    list.append(board[i + k][j + l])
            if not isLineValid(list):
                return False
    return True


if __name__ == '__main__':
    # matrix = [[".","8","7","6","5","4","3","2","1"],
    #           ["2",".",".",".",".",".",".",".","."],
    #           ["3",".",".",".",".",".",".",".","."],
    #           ["4",".",".",".",".",".",".",".","."],
    #           ["5",".",".",".",".",".",".",".","."],
    #           ["6",".",".",".",".",".",".",".","."],
    #           ["7",".",".",".",".",".",".",".","."],
    #           ["8",".",".",".",".",".",".",".","."],
    #           ["9",".",".",".",".",".",".",".","."]]
    matrix = [[".",".",".",".","5",".",".","1","."],
              [".","4",".","3",".",".",".",".","."],
              [".",".",".",".",".","3",".",".","1"],
              ["8",".",".",".",".",".",".","2","."],
              [".",".","2",".","7",".",".",".","."],
              [".","1","5",".",".",".",".",".","."],
              [".",".",".",".",".","2",".",".","."],
              [".","2",".","9",".",".",".",".","."],
              [".",".","4",".",".",".",".",".","."]]
    print(isValidSudoku(matrix))