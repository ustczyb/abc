# coding=utf-8


# abc问题
def abc():
    for a in range(0, 5):
        for b in range(0, 9):
            for c in range(0, 9):
                if 100 * (a + b) + 10 * (b + c) + 2 * c == 532:
                    print(str(a) + " " + str(b) + " " + str(c))


# 最后单词长度
def last_word_len(word):
    word_list = word.split(" ")
    last_word = word_list[-1]
    print(len(last_word))

last_word_len("hello world")