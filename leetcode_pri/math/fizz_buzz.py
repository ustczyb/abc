# coding=utf-8
"""
写一个程序，输出从 1 到 n 数字的字符串表示。

1. 如果 n 是3的倍数，输出“Fizz”；

2. 如果 n 是5的倍数，输出“Buzz”；

3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。
"""
def fizzBuzz(n):
    """
    :type n: int
    :rtype: List[str]
    """
    res = range(1, n + 1)
    for k in range(1, n + 1):
        if k % 3 == 0:
            if k % 5 == 0:
                res[k - 1] = "FizzBuzz"
            else:
                res[k - 1] = "Fizz"
        elif k % 5 == 0:
            res[k - 1] = "Buzz"
        else:
            res[k - 1] = str(k)
    return res


if __name__ == '__main__':
    print(fizzBuzz(15))