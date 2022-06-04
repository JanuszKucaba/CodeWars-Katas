"""
Given a string of words, you need to find the highest scoring word.
Each letter of a word scores points according to its position in the
alphabet: a = 1, b = 2, c = 3 etc.
You need to return the highest scoring word as a string.
If two words score the same, return the word that appears earliest
in the original string. All letters will be lowercase and all inputs
will be valid.
https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/train/python
"""


# 1 solution
def high(x):
    """Takes a sentence and return
    the highest scoring word."""
    x_list = x.split()
    x_num = []
    for item in x_list:
        num = 0
        for char in item:
            num += (ord(char) - 96)
        x_num.append(num)

    max_num = max(x_num)
    idx = x_num.index(max_num)
    return x_list[idx]


# 2 solution
def high2(x):
    """Takes a sentence and return
    the highest scoring word."""
    x_list = x.split()
    x_num = [sum([(ord(char) - 96) for char in item]) for item in x_list]
    return x_list[x_num.index(max(x_num))]


# 3 solution
def high3(x):
    """Takes a sentence and return
    the highest scoring word."""
    return max(x.split(), key=lambda word: sum(ord(ch) - 96 for ch in word))


if __name__ == '__main__':
    print(high('man i need a taxi up to ubud'))
    print(high('what time are we climbing up the volcano'))
    print(high('take me to semynak'))
    print(high('aa b'))
    print(high('b aa'))
    print(high('bb d'))
    print(high('d bb'))
    print()
    print(high2('man i need a taxi up to ubud'))
    print(high2('what time are we climbing up the volcano'))
    print(high2('take me to semynak'))
    print(high2('aa b'))
    print(high2('b aa'))
    print(high2('bb d'))
    print(high2('d bb'))
    print()
    print(high3('man i need a taxi up to ubud'))
    print(high3('what time are we climbing up the volcano'))
    print(high3('take me to semynak'))
    print(high3('aa b'))
    print(high3('b aa'))
    print(high3('bb d'))
    print(high3('d bb'))
