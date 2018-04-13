# coding=utf-8
"""
实现 atoi，将字符串转为整数。

提示：仔细考虑所有的输入情况。如果你想挑战自己，请不要看下面的示例，并尽可能独立思考所有的情况。

说明：这道题解释的比较模糊（即没有指定输入格式）。你需要事先汇总所有的输入情况。



atoi的要求：

在找到第一个非空字符之前，函数需移除掉字符串前面的空格。

从这个非空字符开始，选取一个可选的正号或负号，并将后面跟随尽可能多的数字，这部分字符即为数字的值。

字符串可以在形成整数的字符后包括多余的非数字字符，将这些字符忽略，这些字符对于函数没有影响。

如果字符串中的第一个非空字符不是有效的整数，以及因字符串为空或者因只包含空白字符而导致没有这样的序列存在，则不进行转换。

如果不能执行有效的转换，则返回 0。如果正确的值超过可表示的范围，则返回 INT_MAX（2147483647）或 INT_MIN（-2147483648）。
"""
def myAtoi(str):
    """
    :type str: str
    :rtype: int
    """
    str = str.strip()
    if str == '' or str == '+' or str == '-':
        return 0
    if not str[0].isdigit() and not str[0] == '+' and not str[0] == '-':
        return 0
    for i in range(1, len(str)):
        if not str[i].isdigit():
            str = str[0:i]
            break
    if str == '+' or str == '-':
        return 0
    res = int(str)
    if res > 2147483647:
        return 2147483647
    if res < -2147483648:
        return -2147483648
    return res


if __name__ == '__main__':
    s = "+1"
    print(myAtoi(s))