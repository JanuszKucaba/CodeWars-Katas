"""
Your task is to sort a given string.

Each word in the string will contain a single number.
This number is the position the word should have in the result.
Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
If the input string is empty, return an empty string.
The words in the input String will only contain valid consecutive numbers.
https://www.codewars.com/kata/55c45be3b2079eccff00010f
"""


# long version
def order(sentence):
    """
    Input: string contain words with number.

    Outputs: sorted words based on the number they contain
    """
    if not sentence:
        return ''
    words = sentence.split(' ')
    nums = []
    for idx, word in enumerate(words):
        for let in word:
            if let.isdigit():
                nums.append((int(let), words[idx]))

    sort_nums = sorted(nums)
    res = []
    for item in sort_nums:
        res.append(item[1])

    return ' '.join(res)


# short version
def order2(sentence):
    """
    Input: string contain words with number.

    Outputs: sorted words based on the number they contain
    """
    return ' '.join(sorted(sentence.split(), key=sorted(sentence)))


if __name__ == '__main__':
    print(order("is2 Thi1s T4est 3a"))
    print(order("4of Fo1r pe6ople g3ood th5e the2"))
    print(order(""))
    print()
    print(order("is2 Thi1s T4est 3a"))
    print(order("4of Fo1r pe6ople g3ood th5e the2"))
    print(order(""))
