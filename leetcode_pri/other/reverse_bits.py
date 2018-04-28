# coding=utf-8
"""
颠倒给定的 32 位无符号整数的二进制位。

示例:

输入: 43261596
输出: 964176192
解释: 43261596 的二进制表示形式为 00000010100101000001111010011100 ，
     返回 964176192，其二进制表示形式为 00111001011110000010100101000000 。
进阶:
如果多次调用这个函数，你将如何优化它？
"""


# @param n, an integer
# @return an integer
def reverse_bits(n):
    bin_str = str(bin(n)).replace('0b', '')
    s = 32 - len(bin_str)
    for i in range(s):
        bin_str = '0' + bin_str
    res = int(bin_str[::-1], 2)
    return res

if __name__ == '__main__':
    print(reverse_bits(43261596))